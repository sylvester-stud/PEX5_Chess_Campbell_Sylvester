#!/usr/bin/env python3
"""
This program creates a Chess game using the python console and object oriented programming concepts.

The game will use 8 classes involving the game, the pieces, and the player
CS 210, Introduction to Programming
"""

__author__ = "Cage Campbell & Christian Sylvester"  # Your name. Ex: John Doe
__section__ = "M6"  # Your section. Ex: M1
__instructor__ = "Dr. Bower"  # Your instructor. Ex: Lt Col Doe
__date__ = "05 Dec 2017"  # Today's date. Ex: 25 Dec 2017
__documentation__ = """ None """  # Multiple lines OK with triple quotes


def main():
    """
    Contains the main program for the PEX
    """

    player1 = Player("Name1", "White")
    player2 = Player("Opponent", "Black")
    game_board = Board(player1, player2)
    print(game_board.board)


def Chess_String(board):
    """ Prints a Chess Board using information from the Board object."""


class Board:
    """ Initializes the game board, tracks each player's moves, and monitors the status of the chess game."""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        pawn1 = Pawn(player1)
        pawn2 = Pawn(player2)
        self.board = [(), (), (), (), (), (), (), (), ()] * 9
        for i in range(9, 18):
            self.board[i] = pawn1.type()
        for i in range(63, 72):
            self.board[i] = pawn2.type()


class Player:
    """ Tracks the properties of each player."""

    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.__name

    def color(self):
        return self.__color

    def switch_colors(self):
        if self.color == "Black":
            self.__color = "White"
        else:
            self.__color = "White"


class Pawn:
    """ A pawn piece in the Chess game. """

    def __init__(self, owner):
        """
        Initializes a new Player with a name and a color.
        :param str name: the player's name
        :param str color: the player's color
        """
        self.__owner = owner  # type: Player
        self.__type = "Pawn"

    def __str__(self):
        """
        Returns a simple string representation of the player, ie, the player name.
        :return:
        """
        return "{}'s Pawn".format(self.owner)

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


class Rook:
    """ Creates a Rook object."""


class Knight:
    """ Creates a Knight object."""


class Bishop:
    """ Creates a Bishop object."""


class Queen:
    """ Creates a Queen object."""


class King:
    """ Creates a King object."""


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
