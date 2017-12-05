#!/usr/bin/env python3
"""
This program creates a Chess game using the python console and object oriented programming concepts.

The game will use 8 classes involving the game, the pieces, and the player
CS 210, Introduction to Programming
"""

import math
import tkinter as tk

__author__ = "Cage Campbell & Christian Sylvester"
__section__ = "M6"
__instructor__ = "Dr. Bower"
__date__ = "05 Dec 2017"
__documentation__ = """ None """

"""Classes nearly complete; provisions needed for killing other pieces, and not letting pieces move through(wrap 
   around)borders. Other things needed: GUI/Adv. features (if desired)."""


def main():
    """
    Contains the main program for the PEX
    """

    program = DrawChessBoard()
    program.window.mainloop()
    player1 = Player("Name1", "White")
    player2 = Player("Opponent", "Black")
    game_board = Board(player1, player2)
    # Example move: game_board.board[10].move(player1, 24, game_board, 8)
    print(game_board.print_board())


class DrawChessBoard:
    """ An App that serves as the GUI for a Chess game. """

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chess")

        # View / Control
        self.canvas = None  # type: tk.Canvas
        self.create_widgets()

    def mouse_click(self):
        cv = self.Canvas()

    def create_widgets(self):
        lbl = tk.Label(self.window, text="Chess Board")
        lbl.pack()

        # Canvas
        self.canvas = tk.Canvas(self.window, bg="white")
        self.canvas.pack(fill=tk.BOTH)
        self.create_canvas()

    def create_canvas(self):
        self.canvas.config(width=600, height=600)
        width = int(self.canvas["width"]) + 2
        height = int(self.canvas["height"]) + 2
        color = "White"
        for r in range(8):
            for n in range(8):
                self.canvas.create_rectangle((n * width // 8), r * height // 8, (n + 1) * width // 8,
                                             (r + 1) * height // 8, fill=color, outline="Black")
                if color == "White":
                    color = "Black"
                else:
                    color = "White"
            if color == "White":
                color = "Black"
            else:
                color = "White"
            r += 1


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
        :param str owner: The player who owns the pawn.
        """
        self.__owner = owner  # type: Player
        self.__type = "Pawn"
        self.__played = False  # tracks whether or not a pawn has moved (first move can be up to two spaces)
        self.__color = owner.color()

    @property
    def owner(self):
        """
        Returns the owner of the pawn
        :return: the owner
        :rtype: Player
        """
        return self.__owner

    def type(self):
        return self.__type

    def color(self):
        return self.__color

    def move(self, player, click, game, location):
        """ Moves a pawn to the clicked location (rules-permitting).
        :param Player player: The player moving.
        :param int click: The tile number of the desired space to move to (clicked tile).
        :param Board game: The game in which to move the pawn.
        :param int location: The tile number of the current location.
        """
        pawn = game.board[location]
        if game.current_player is player and player.color() is pawn.color() and (click - location) % 8 == 0:
            if self.__played is False and math.fabs(click - location) == 16 or player.color() == "White" and click - \
                    location == 8 or player.color() == "Black" and location - click == 8:
                pawn = game.board.pop(location)
                game.board.insert(location, ())
                game.board[click] = pawn
                self.__played = True
        else:
            pass


class Rook:
    """ Creates a Rook object."""

    def __init__(self, owner):
        """

        :return:
        """
        self.__owner = owner
        self.__type = "Rook"

    @property
    def type(self):
        return self.__type

    def move(self, location, game, click):
        """

        :return:
        """
        if (click - location) % 8 == 0 or (location % 8 - click % 8) < 8:
            rook = game.board.pop(location)
            game.board.insert(location, ())
            game.board[click] = rook
        else:
            pass


class Knight:
    """ Creates a Knight object."""

    def __init__(self, owner):
        """
        Initializes a new Player with a name and a color.
        :param str name: the player's name
        :param str color: the player's color
        """
        self.__owner = owner  # type: Player
        self.__type = "Knight"
        self.__color = owner.color()

    @property
    def owner(self):
        """
        Returns the owner of the pawn
        :return: the owner
        :rtype: Player
        """
        return self.__owner

    def type(self):
        return self.__type

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
        if game.current_player is player and player.color() is knight.color():
            if math.fabs(click - location) == 17 or math.fabs(click - location) == 15:
                knight = game.board.pop(location)
                game.board.insert(location, ())
                game.board[click] = knight
        else:
            pass


class Bishop:
    """ Creates a Bishop object."""

    def __init__(self, owner):
        """
        Initializes a new Player with a name and a color.
        :param str name: the player's name
        :param str color: the player's color
        """
        self.__owner = owner  # type: Player
        self.__type = "Bishop"
        self.__color = owner.color()

    @property
    def owner(self):
        """
        Returns the owner of the pawn
        :return: the owner
        :rtype: Player
        """
        return self.__owner

    def type(self):
        return self.__type

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
        if game.current_player is player and player.color() is bishop.color():
            if (click - location) % 9 == 0 or (click - location) % 7 == 0:
                bishop = game.board.pop(location)
                game.board.insert(location, ())
                game.board[click] = bishop
        else:
            pass


class Queen:
    """ Creates a Queen object."""

    def __init__(self, owner):
        """
        Initializes a new Player with a name and a color.
        :param str name: the player's name
        :param str color: the player's color
        """
        self.__owner = owner  # type: Player
        self.__type = "Queen"
        self.__color = owner.color()

    @property
    def owner(self):
        """
        Returns the owner of the pawn
        :return: the owner
        :rtype: Player
        """
        return self.__owner

    def type(self):
        return self.__type

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
        if game.current_player is player and player.color() is queen.color():
            if (click - location) % 8 == 0 or (location % 8 - click % 8) < 8 or (click - location) % 9 == 0 or (
                        click - location) % 7 == 0:
                queen = game.board.pop(location)
                game.board.insert(location, ())
                game.board[click] = queen
        else:
            pass


class King:
    """ Creates a King object."""

    def __init__(self, owner):
        """
        Initializes a new Player with a name and a color.
        :param str name: the player's name
        :param str color: the player's color
        """
        self.__owner = owner  # type: Player
        self.__type = "King"
        self.__color = owner.color()

    @property
    def owner(self):
        """
        Returns the owner of the pawn
        :return: the owner
        :rtype: Player
        """
        return self.__owner

    def type(self):
        return self.__type

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
        if game.current_player is player and player.color() is king.color():
            if math.fabs(click - location) == 1 or math.fabs(click - location) == 7 or math.fabs(
                            click - location) == 8 or math.fabs(click - location) == 9:
                king = game.board.pop(location)
                game.board.insert(location, ())
                game.board[click] = king
        else:
            pass


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
# 1427a7e2b045a7428ffc5012d0f0dcecdfd4af0547ddb0da1b6d9e4b0eef7703 ppntrpnzcoryy
