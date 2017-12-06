#!/usr/bin/env python3
"""
This program creates a Chess game using the python console and object oriented programming concepts.

The game will use 8 classes involving the game, the pieces, and the player
CS 210, Introduction to Programming
"""

import math
import turtle
from easygui import msgbox

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

    player1 = Player("Name1", "White")
    player2 = Player("Opponent", "Black")
    game_board = Board(player1, player2)
    # Example move: game_board.board[10].move(player1, 24, game_board, 8)
    print(game_board.print_board())
    board_gui(game_board, player1, player2)
    print(game_board.board[1].type)
    print(game_board.board[0].type)


def board_gui(board, player1, player2):
    window = turtle.Screen()
    artist = turtle.Turtle()
    piece = turtle.Turtle()
    writer = turtle.Turtle()

    # Register all Chess Pieces in GUI.
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

    window.setup(WIDTH, HEIGHT + 100)
    artist.speed("fastest")
    window.tracer(0, 0)
    writer.up()
    writer.ht()
    writer.goto(0, HEIGHT // 2)
    writer.down()

    draw_board(window, artist, piece, writer, board)

    winner = None
    while winner is None:
        location = 71
        while location == 71:
            location = get_location(window, artist)
        click = location
        if board.board[location] != () and board.board[location].type == "Pawn":
            print(board.board[location].check_moves(board.board[location].owner, board, location))
        while click == location:
            click = get_location(window, artist)
        if board.board[location] == ():
            pass
        else:
            good_move = board.board[location].move(board.current_player, click, board, location)
            if good_move is None:
                board.new_turn()
        winner = check_winner(board)
        draw_board(window, artist, piece, writer, board)
    msgbox("{} wins!".format(winner))
    window.mainloop()


def draw_board(window, artist, piece, writer, board):
    color = "Black"
    x = -WIDTH // 2
    y = HEIGHT // 2 - 50
    counter = 0
    while counter < 74:
        if counter % 9 != 0:
            Draw_Square(artist, x, y, 100, color)
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
        if tile == ():
            piece.color("White")
            piece.shape("triangle")
        elif tile.type == "Pawn":
            if tile.color == "White":
                piece.shape(white_pawn)
            else:
                piece.shape(black_pawn)
        elif tile.type == "Rook":
            if tile.color == "White":
                piece.shape(white_rook)
            else:
                piece.shape(black_rook)
        elif tile.type == "Knight":
            if tile.color == "White":
                piece.shape(white_knight)
            else:
                piece.shape(black_knight)
        elif tile.type == "Bishop":
            if tile.color == "White":
                piece.shape(white_bishop)
            else:
                piece.shape(black_bishop)
        elif tile.type == "Queen":
            if tile.color == "White":
                piece.shape(white_queen)
            else:
                piece.shape(black_queen)
        else:
            if tile.color == "White":
                piece.shape(white_king)
            else:
                piece.shape(black_king)
        piece.stamp()

    # Writer changes
    writer.undo()
    writer.write("{}'s turn".format(board.current_player.color), False, align="Center", font=("Arial", 20, "normal"))

    window.update()
    artist.penup()
    artist.ht()


def get_location(window, artist):
    window.onscreenclick(artist.goto)
    window.update()
    x, y = artist.xcor(), artist.ycor() + 50
    x_int = math.ceil(x / 100) + 3
    y_int = (math.fabs(math.ceil(y / 100) - 4))
    location = int(y_int * 8 + x_int)
    return location


def Draw_Square(turtle, x, y, width, color):
    turtle.seth(0)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(width)
        turtle.left(90)
    turtle.end_fill()


def check_winner(board):
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
        return self.__current_player

    def new_turn(self):
        if self.__current_player == self.player1:
            self.__current_player = self.player2
        else:
            self.__current_player = self.player1

    def print_board(self):
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
        self.__name = name
        self.__color = color
        self.__wins = 0
        self.__losses = 0

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    def wins(self):
        return self.__wins

    def losses(self):
        return self.losses()


class Pawn:
    """ A pawn piece in the Chess game. """

    def __init__(self, owner):
        """
        Initializes a new Player with a name and a color.
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
        return self.__type

    @property
    def color(self):
        return self.__color

    def move(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
        :param Player player: The player moving.
        :param int click: The tile number of the desired space to move to (clicked tile).
        :param Board game: The game in which to move the pawn.
        :param int location: The tile number of the current location.
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
        :param Player owner: The owning player
        """
        self.__owner = owner
        self.__type = "Rook"
        self.__color = owner.color

    @property
    def type(self):
        return self.__type

    @property
    def color(self):
        return self.__color

    def move(self, player, click, game, location):
        """

        :return:
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
        return self.__type

    @property
    def color(self):
        return self.__color

    def move(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
        :param Player player: The player moving.
        :param int click: The tile number of the desired space to move to (clicked tile).
        :param Board game: The game in which to move the pawn.
        :param int location: The tile number of the current location.
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
        return self.__type

    @property
    def color(self):
        return self.__color

    def move(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
        :param Player player: The player moving.
        :param int click: The tile number of the desired space to move to (clicked tile).
        :param Board game: The game in which to move the pawn.
        :param int location: The tile number of the current location.
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
        return self.__type

    @property
    def color(self):
        return self.__color

    def move(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
        :param Player player: The player moving.
        :param int click: The tile number of the desired space to move to (clicked tile).
        :param Board game: The game in which to move the pawn.
        :param int location: The tile number of the current location.
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
        return self.__type

    @property
    def color(self):
        return self.__color

    def move(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
        :param Player player: The player moving.
        :param int click: The tile number of the desired space to move to (clicked tile).
        :param Board game: The game in which to move the pawn.
        :param int location: The tile number of the current location.
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
