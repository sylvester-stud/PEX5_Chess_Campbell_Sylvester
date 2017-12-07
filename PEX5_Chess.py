#!/usr/bin/env python3
"""
This program creates a Chess game using the python console and object oriented programming concepts.

The game will use 8 classes involving the game, the pieces, and the player
CS 210, Introduction to Programming
"""

import math
import turtle
from easygui import msgbox, enterbox

__author__ = "Cage Campbell & Christian Sylvester"
__section__ = "M6"
__instructor__ = "Dr. Bower"
__date__ = "05 Dec 2017"
__documentation__ = """ None """

"""Classes nearly complete; provisions needed for killing other pieces, and not letting pieces move through(wrap 
   around)borders. Other things needed: GUI/Adv. features (if desired)."""

# Window Properties:
WIDTH = 800
HEIGHT = 800

# Attach piece images to respective file names.
white_pawn = "./Chess Pieces/White-Pawn.gif"
white_rook = "./Chess Pieces/White-Rook.gif"
white_knight = "./Chess Pieces/White-Knight.gif"
white_bishop = "./Chess Pieces/White-Bishop.gif"
white_queen = "./Chess Pieces/White-Queen.gif"
white_king = "./Chess Pieces/White-King.gif"
black_pawn = "./Chess Pieces/Black-Pawn.gif"
black_rook = "./Chess Pieces/Black-Rook.gif"
black_knight = "./Chess Pieces/Black-Knight.gif"
black_bishop = "./Chess Pieces/Black-Bishop.gif"
black_queen = "./Chess Pieces/Black-Queen.gif"
black_king = "./Chess Pieces/Black-King.gif"


def main():
    """
    Contains the main program for the PEX
    """

    # Initializes the players for the game
    p1_name = enterbox("Enter Player 1 name", "P1 name", default="Name1")
    player1 = Player(p1_name, "White")
    p2_name = enterbox("Enter Player 2 name", "P2 name", default="Name2")
    player2 = Player(p2_name, "Black")

    # Initializes the board and prints the initial condition to the console
    game_board = Board(player1, player2)
    print(game_board.print_board())
    board_gui(game_board, player1, player2)
    print(game_board.board[1].type)
    print(game_board.board[0].type)


def board_gui(board, player1, player2):
    """
    Plays the game as a gui
    :param board: Board object for the game
    :param player1: Determines the first player
    :param player2: Determines the second player
    """
    # Set-up for the turtle-based gui
    window = turtle.Screen()
    artist = turtle.Turtle()
    piece = turtle.Turtle()
    writer = turtle.Turtle()

    # Register all Chess Piece Images in GUI.
    window.register_shape(white_pawn)
    window.register_shape(white_rook)
    window.register_shape(white_bishop)
    window.register_shape(white_knight)
    window.register_shape(white_queen)
    window.register_shape(white_king)
    window.register_shape(black_pawn)
    window.register_shape(black_rook)
    window.register_shape(black_knight)
    window.register_shape(black_bishop)
    window.register_shape(black_queen)
    window.register_shape(black_king)

    # Window and writer initialization
    window.setup(WIDTH, HEIGHT + 100)
    artist.speed("fastest")
    window.tracer(0, 0)
    writer.up()
    writer.ht()
    writer.goto(0, HEIGHT // 2)
    writer.down()

    draw_board(window, artist, piece, writer, board)  # Draws the first board

    winner = None
    while winner is None:  # Plays until a winner is declared
        location = 71  # Black magic
        while location == 71:  # Grabs the mouse click for the piece
            location = get_location(window, artist)
        click = location
        # try:  # For testing of the check_moves of each piece
        #     print(board.board[location].check_moves(board.board[location].owner, board, location))
        # except:
        #     pass
        while click == location:  # Grabs the mouse click for the move
            click = get_location(window, artist)
        if board.board[location] == ():
            pass
        else:
            # Moves the selected piece and advances the turn if a valid move was made
            good_move = board.board[location].move(board.current_player, click, board, location)
            if good_move is None:
                board.new_turn()
        winner = check_winner(board)  # Checks for the winner
        draw_board(window, artist, piece, writer, board)
    msgbox("{} wins!".format(winner.name))  # Declares winner
    window.mainloop()


def draw_board(window, artist, piece, writer, board):
    """
    Draws a board in its current state
    :param Screen window: The window that the gui hosted game is played in
    :param Turtle artist: The turtle which draws the board
    :param Turtle piece: The turtle which manipulates the pieces
    :param Turtle writer: The turtle which writes the game state
    :param Board board: The host board
    """
    color = "Black"
    x = -WIDTH // 2
    y = HEIGHT // 2 - 50
    counter = 0
    while counter < 74:  # Initializes the full visual board (unknown constant)
        if counter % 9 != 0:
            draw_square(artist, x, y, 100, color)
            x += 100
        else:
            y -= 100
            x = -WIDTH // 2
        counter += 1
        if color == "White":
            color = "Black"
        else:
            color = "White"
    window.update()

    # Print pieces to board GUI.
    for tile in board.board:
        piece.penup()
        location = board.board.index(tile)
        x = (location % 8) * 100 - 350
        y = -(location + 1) // 8 * (HEIGHT // 8) + HEIGHT // 2
        piece.goto(x, y)

        # Puts all of the pieces in their respective locations
        if tile == ():  # Empty spaces
            piece.color("White")
            piece.shape("triangle")
        elif tile.type == "Pawn":  # Pawns
            if tile.color == "White":
                piece.shape(white_pawn)
            else:
                piece.shape(black_pawn)
        elif tile.type == "Rook":  # Rooks
            if tile.color == "White":
                piece.shape(white_rook)
            else:
                piece.shape(black_rook)
        elif tile.type == "Knight":  # Knights
            if tile.color == "White":
                piece.shape(white_knight)
            else:
                piece.shape(black_knight)
        elif tile.type == "Bishop":  # Bishops
            if tile.color == "White":
                piece.shape(white_bishop)
            else:
                piece.shape(black_bishop)
        elif tile.type == "Queen":  # Queens
            if tile.color == "White":
                piece.shape(white_queen)
            else:
                piece.shape(black_queen)
        else:  # Kings
            if tile.color == "White":
                piece.shape(white_king)
            else:
                piece.shape(black_king)

        piece.stamp()  # Places the image of the piece

    # Writer changes
    writer.undo()
    writer.write("{}'s turn".format(board.current_player.color), False, align="Center", font=("Arial", 20, "normal"))

    window.update()
    artist.penup()
    artist.ht()


def get_location(window, artist):
    """
    Gets the location of the mouse click for the gui program
    :param Window window: The window in which to grab the mouse location
    :param Turtle artist: The turtle which uses the information
    :return: location of the mouse click
    :rtype: int
    """
    window.onscreenclick(artist.goto)
    window.update()
    x, y = artist.xcor(), artist.ycor() + 50
    x_int = math.ceil(x / 100) + 3
    y_int = (math.fabs(math.ceil(y / 100) - 4))
    location = int(y_int * 8 + x_int)
    return location


def draw_square(tom, x, y, width, color):
    """
    Draws the empty squares for the board
    :param Turtle tom: Turtle which draws the squares
    :param int x: The x location of the square
    :param int y: The y location of the square
    :param int width: The length of a side of the square
    :param str color: The color of the square
    """
    tom.seth(0)
    tom.penup()
    tom.goto(x, y)
    tom.pendown()
    tom.color(color)
    tom.begin_fill()
    for i in range(4):
        tom.fd(width)
        tom.left(90)
    tom.end_fill()


def check_winner(board):
    """
    Determines if there is a winner in the game
    :param Board board: The game being checked
    :return: The winning player
    :rtype: Player
    """
    kings = []
    for space in board.board:
        if type(space) == King:
            kings.append(space)
    if len(kings) != 2:
        color = kings[0].color
        if board.player1.color == color:
            return board.player1
        else:
            return board.player2


class Board:
    """ Initializes the game board, tracks each player's moves, and monitors the status of the chess game."""

    def __init__(self, player1, player2):
        """
        Init of the Board class
        :param Player player1: Player 1 of the game
        :param Player player2: Player 2 of the game
        """
        self.player1 = player1
        self.player2 = player2
        self.__current_player = player1

        # Pawn initialization
        pawns1_list = [0, 1, 2, 3, 4, 5, 6, 7]
        p1_pawns = {}
        for name in pawns1_list:
            p1_pawns[name] = Pawn(player1)
        p2_pawns = {}
        for name in pawns1_list:
            p2_pawns[name] = Pawn(player2)

        # Pawn Placement
        self.board = [(), (), (), (), (), (), (), ()] * 8
        for i in range(8, 16):
            self.board[i] = p1_pawns[i - 8]
        for i in range(48, 56):
            self.board[i] = p2_pawns[i - 48]

        # Rook Initialization/Placement
        self.board[0] = Rook(player1)
        self.board[7] = Rook(player1)
        self.board[56] = Rook(player2)
        self.board[63] = Rook(player2)

        # Knight Initialization/Placement
        self.board[1] = Knight(player1)
        self.board[6] = Knight(player1)
        self.board[57] = Knight(player2)
        self.board[62] = Knight(player2)

        # Bishop Initialization/Placement
        self.board[2] = Bishop(player1)
        self.board[5] = Bishop(player1)
        self.board[58] = Bishop(player2)
        self.board[61] = Bishop(player2)

        # Queen Initialization/Placement
        self.board[4] = Queen(player1)
        self.board[59] = Queen(player2)

        # King Initialization/Placement
        self.board[3] = King(player1)
        self.board[60] = King(player2)

    @property
    def current_player(self):
        """
        Read only current player property
        :return: current player
        :rtype: Player
        """
        return self.__current_player

    def new_turn(self):
        """
        Changes the current player
        """
        if self.__current_player == self.player1:
            self.__current_player = self.player2
        else:
            self.__current_player = self.player1

    def print_board(self):
        """
        Prints the board in its current status
        """
        print(self.board[0:8])
        print(self.board[8:16])
        print(self.board[16:24])
        print(self.board[24:32])
        print(self.board[32:40])
        print(self.board[40:48])
        print(self.board[48:56])
        print(self.board[56:64])


class Player:
    """ Tracks the properties of each player."""

    def __init__(self, name, color):
        """
        Init of the Player class
        :param str name: The player's name
        :param str color: The player's color
        """
        self.__name = name
        self.__color = color
        self.__wins = 0
        self.__losses = 0

    @property
    def name(self):
        """
        The read only name property
        :return: name of the player
        :rtype: str
        """
        return self.__name

    @property
    def color(self):
        """
        The read only color property of the class
        :return: The player object's color
        :rtype: str
        """
        return self.__color

    @property
    def wins(self):
        """
        The read only wins property
        :return: Player's wins
        :rtype: int
        """
        return self.__wins

    @property
    def losses(self):
        """
        The read only wins property
        :return: Player's wins
        :rtype: int
        """
        return self.losses()


class Pawn:
    """ A pawn piece in the Chess game. """

    def __init__(self, owner):
        """
        Initializes a pawn with an owner.
        :param Player owner: The player who owns the pawn.
        """
        self.__owner = owner  # type: Player
        self.__type = "Pawn"
        self.__played = False  # tracks whether or not a pawn has moved (first move can be up to two spaces)
        self.__color = owner.color

    @property
    def owner(self):
        """
        Returns the owner of the pawn
        :return: the owner
        :rtype: Player
        """
        return self.__owner

    @property
    def type(self):
        """
        The read only type of the pawn
        :return: The type of the pawn
        :rtype: str
        """
        return self.__type

    @property
    def color(self):
        """
        The read only color property
        :return: The color of the pawn
        :rtype: str
        """
        return self.__color

    def move(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
        :param Player player: The player moving.
        :param int click: The tile number of the desired space to move to (clicked tile).
        :param Board game: The game in which to move the pawn.
        :param int location: The tile number of the current location.
        :return: If invalid move, returns string "Invalid"
        """
        pawn = game.board[location]  # type: Pawn
        if game.current_player is player and player.color is pawn.color and (click - location) % 8 == 0 and \
                        game.board[click] == ():
            if self.__played is False and math.fabs(click - location) == 16 or player.color == "White" and click - \
                    location == 8 or player.color == "Black" and location - click == 8:
                pawn = game.board.pop(location)
                game.board.insert(location, ())
                game.board[click] = pawn
                self.__played = True
        else:
            good_move = self.attack(player, click, game, location)
            return good_move

    def check_moves(self, player, game, location):
        """
        Checks valid moves for the pawn
        :param Player player: The owning player of the pawn
        :param Board game: The hosting board
        :param int location: The location of the pawn
        :return: Possible moves
        :rtype: list[int]
        """
        good_moves = []
        pawn = game.board[location]  # type: Pawn
        for click in range(len(game.board)):
            if game.current_player is player and player.color is pawn.color and game.board[click] == ():
                if self.__played is False and math.fabs(click - location) == 16 or player.color == "White" and click - \
                        location == 8 or player.color == "Black" and location - click == 8:
                    good_moves.append(click)
                elif game.current_player is player and player.color is pawn.color and game.board[click] != () and \
                        abs(click - location) < 10 and ((click - location) % 9 == 0 or (click - location) % 7 == 0) and\
                        game.board[click].color != player.color:
                    good_moves.append(click)
        return good_moves

    def attack(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
                :param Player player: The player moving.
                :param int click: The tile number of the desired space to move to (clicked tile).
                :param Board game: The game in which to move the pawn.
                :param int location: The tile number of the current location.
                """
        pawn = game.board[location]  # type: Pawn
        if game.current_player is player and player.color is pawn.color and game.board[click] != () and \
                        abs(click - location) < 10 and ((click - location) % 9 == 0 or (click - location) % 7 == 0) and\
                        game.board[click].color != player.color:
            pawn = game.board.pop(location)
            game.board.insert(location, ())
            game.board[click] = pawn
            self.__played = True
        else:
            return "Invalid"


class Rook:
    """ Creates a Rook object."""

    def __init__(self, owner):
        """
        Initializes the Rook object
        :param Player owner: The owning player
        """
        self.__owner = owner
        self.__type = "Rook"
        self.__color = owner.color

    @property
    def type(self):
        """
        The read only property of the type
        :return: That it is a rook
        :rtype: str
        """
        return self.__type

    @property
    def color(self):
        """
        The color property
        :return: color of the rook
        :rtype: str
        """
        return self.__color

    def move(self, player, click, game, location):
        """
        Moves the Rook
        :param Player player: The owning player of the rook
        :param int click: The target of the move
        :param Board game: The hosting board object
        :param int location: The current location of the rook
        :return: String "Invalid if the move is invalid"
        """
        if ((click - location) % 8 == 0 or abs(location // 8) == click // 8) and \
                (game.board[click] == () or game.board[click].color != player.color):
            rook = game.board.pop(location)
            game.board.insert(location, ())
            game.board[click] = rook
        else:
            return "Invalid"


class Knight:
    """ Creates a Knight object."""

    def __init__(self, owner):
        """
        Initializes a new Player with a name and a color.
        :param Player owner: the player
        """
        self.__owner = owner
        self.__type = "Knight"
        self.__color = owner.color

    @property
    def owner(self):
        """
        Returns the owner
        :return: the owner
        :rtype: Player
        """
        return self.__owner

    @property
    def type(self):
        """
        The read only type property
        :return: The type of the object
        :rtype: str
        """
        return self.__type

    @property
    def color(self):
        """
        The read only color property
        :return: The color of the Knight
        :rtype: str
        """
        return self.__color

    def move(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
        :param Player player: The player moving.
        :param int click: The tile number of the desired space to move to (clicked tile).
        :param Board game: The game in which to move the knight.
        :param int location: The tile number of the current location.
        :return: Returns "Invalid" if no valid move is made
        """
        knight = game.board[location]
        if (game.board[click] == () or game.board[click].color != player.color) and game.current_player is player and \
                        player.color is knight.color:
            if abs(click - location) == 17 or abs(click - location) == 15 or abs(click - location) == 10 or \
                            abs(click - location) == 6:
                knight = game.board.pop(location)
                game.board.insert(location, ())
                game.board[click] = knight
            else:
                return "Invalid"
        else:
            return "Invalid"


class Bishop:
    """ Creates a Bishop object."""

    def __init__(self, owner):
        """
        Initializes a new Player with a name and a color.
        :param Player owner: the player who owns the bishop
        """
        self.__owner = owner  # type: Player
        self.__type = "Bishop"
        self.__color = owner.color

    @property
    def owner(self):
        """
        Returns the owner of the pawn
        :return: the owner
        :rtype: Player
        """
        return self.__owner

    @property
    def type(self):
        """
        The read only type property
        :return: The type of the piece
        :rtype: str
        """
        return self.__type

    @property
    def color(self):
        """
        The read only color property
        :return: The color of the bishop
        :rtype: str
        """
        return self.__color

    def move(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
        :param Player player: The player moving.
        :param int click: The tile number of the desired space to move to (clicked tile).
        :param Board game: The game in which to move the bishop.
        :param int location: The tile number of the current location.
        :return: "Invalid" if no valid move was played
        """
        bishop = game.board[location]
        if (game.board[click] == () or game.board[click].color != player.color) and game.current_player is player and \
                        player.color is bishop.color:
            if (click - location) % 9 == 0 or (click - location) % 7 == 0:
                bishop = game.board.pop(location)
                game.board.insert(location, ())
                game.board[click] = bishop
            else:
                return "Invalid"
        else:
            return "Invalid"

    def check_moves(self, player, game, location):
        """
        Checks for the possible moves
        :param player:
        :param game:
        :param location:
        :return: The possible moves
        :rtype: list[int]
        """
        good_moves = []
        king = game.board[location]  # type: King
        for click in range(len(game.board)):
            if game.current_player is player and player.color is king.color and\
                    (game.board[click] == () or game.board[click].color != king.color) and\
                    (click - location) % 9 == 0 or (click - location) % 7 == 0:
                good_moves.append(click)
        return good_moves


class Queen:
    """ Creates a Queen object."""

    def __init__(self, owner):
        """
        Initializes a new Player with a name and a color.
        :param Player owner: The owning player
        """
        self.__owner = owner
        self.__type = "Queen"
        self.__color = owner.color

    @property
    def owner(self):
        """
        Returns the owner of the pawn
        :return: the owner
        :rtype: Player
        """
        return self.__owner

    @property
    def type(self):
        """
        The read only type property
        :return: The type of the piece
        :rtype: str
        """
        return self.__type

    @property
    def color(self):
        """
        The read only color property
        :return: The color of the queen
        :rtype: str
        """
        return self.__color

    def move(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
        :param Player player: The player moving.
        :param int click: The tile number of the desired space to move to (clicked tile).
        :param Board game: The game in which to move the queen.
        :param int location: The tile number of the current location.
        :return: Returns "Invalid" if no valid move is detected
        """
        queen = game.board[location]
        if (game.board[click] == () or game.board[click].color != player.color) and game.current_player is player and \
                        player.color is queen.color:
            if (click - location) % 8 == 0 or abs(location // 8) == click // 8 or (click - location) % 9 == 0 or \
                                    (click - location) % 7 == 0:
                queen = game.board.pop(location)
                game.board.insert(location, ())
                game.board[click] = queen
            else:
                return "Invalid"
        else:
            return "Invalid"

    def check_moves(self, player, game, location):
        """
        Checks for the possible moves of the queen
        :param Player player: The owning player
        :param Board game: The hosting game
        :param int location: The current location of the queen
        :return: Possible moves
        :rtype: list[int]
        """
        good_moves = []
        queen = game.board[location]  # type: Queen
        for click in range(len(game.board)):
            if game.current_player is player and player.color is queen.color and\
                    (game.board[click] == () or game.board[click].color != queen.color) and\
                    (click - location) % 8 == 0 or abs(location // 8) == click // 8 or (click - location) % 9 == 0 or \
                    (click - location) % 7 == 0:
                good_moves.append(click)
        return good_moves


class King:
    """ Creates a King object."""

    def __init__(self, owner):
        """
        Initializes a new Player with a name and a color.
        :param Player owner: The owning Player
        """
        self.__owner = owner  # type: Player
        self.__type = "King"
        self.__color = owner.color

    @property
    def owner(self):
        """
        Returns the owner of the pawn
        :return: the owner
        :rtype: Player
        """
        return self.__owner

    @property
    def type(self):
        """
        The read only type property
        :return: The type of the piece
        :rtype: str
        """
        return self.__type

    @property
    def color(self):
        """
        The read only color property
        :return: The color of the king
        :rtype: str
        """
        return self.__color

    def move(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
        :param Player player: The player moving.
        :param int click: The tile number of the desired space to move to (clicked tile).
        :param Board game: The game in which to move the king.
        :param int location: The tile number of the current location.
        :return: "Invalid" if the move is not valid
        """
        king = game.board[location]
        if (game.board[click] == () or game.board[click].color != player.color) and game.current_player is player and \
                        player.color is king.color:
            if math.fabs(click - location) == 1 or math.fabs(click - location) == 7 or math.fabs(
                            click - location) == 8 or math.fabs(click - location) == 9:
                king = game.board.pop(location)
                game.board.insert(location, ())
                game.board[click] = king
            else:
                return "Invalid"
        else:
            return "Invalid"

    def check_moves(self, player, game, location):
        """
        Finds the possible moves of the king
        :param Player player: The owning player
        :param Board game: The hosting game
        :param int location: The current location of the king
        :return: The possible moves
        :rtype: list[int]
        """
        good_moves = []
        king = game.board[location]  # type: King
        for click in range(len(game.board)):
            if game.current_player is player and player.color is king.color and\
                    (game.board[click] == () or game.board[click].color != king.color) and\
                    math.fabs(click - location) == 1 or math.fabs(click - location) == 7 or\
                    math.fabs(click - location) == 8 or math.fabs(click - location) == 9:
                good_moves.append(click)
        return good_moves


# ---DO NOT EDIT---
if __name__ == "__main__":
    print(__doc__.strip())
    b = b'CmltcG9ydCBnZXRwYXNzLCBoYXNobGliLCBjb2RlY3MsIHN0cmluZyBhcyBfX1MKdSA9IGdldHBhc3MuZ2V0dXNlcigpCmggPSBoYXN' + \
        b'obGliLnNoYTI1Nih1LmVuY29kZSgpKS5oZXhkaWdlc3QoKQpyID0gY29kZWNzLmVuY29kZSh1Lmxvd2VyKCkudHJhbnNsYXRlKHtvcm' + \
        b'Qoayk6IE5vbmUgZm9yIGsgaW4gX19TLmRpZ2l0c30pLnJlcGxhY2UoJy4nLCcnKSwgJ3JvdF8xMycpCndpdGggb3BlbihfX2ZpbGVfX' + \
        b'ywgInIiKSBhcyBmOgogICAgaWYgaCBub3QgaW4gZi5yZWFkKCk6CiAgICAgICAgd2l0aCBvcGVuKF9fZmlsZV9fLCAiYSIpIGFzIGY6' + \
        b'CiAgICAgICAgICAgIHByaW50KCIjIiwgaCwgciwgZmlsZT1mKQo='
    try:
        import base64

        eval(compile(base64.b64decode(b), '<string>', "exec"))
    except:
        pass
    finally:
        main()  # 158ae6d65fa398f102e6d805c3fd57ae0779c78e37c85d71bf6c34aac77f354a ppuevfgvnaflyirfg
        # 1427a7e2b045a7428ffc5012d0f0dcecdfd4af0547ddb0da1b6d9e4b0eef7703 pp
