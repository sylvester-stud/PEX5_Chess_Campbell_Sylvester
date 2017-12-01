#!/usr/bin/env python3
"""
This is a test
This program creates a Chess game using the python console and object oriented programming concepts.

The game will use 8 classes involving the game, the pieces, and the player
CS 210, Introduction to Programming
"""

__author__ = "Cage Campbell & Christian Sylvester"
__section__ = "M6"
__instructor__ = "Dr. Bower"
__date__ = "05 Dec 2017"
__documentation__ = """ None """


def main():
    """
    Contains the main program for the PEX
    """

    player1 = Player("Name1", "White")
    player2 = Player("Name2", "Black")
    game_board = Board(player1, player2)
    print(game_board.board)
    print(game_board.board[9].type())
    print(game_board.board[9].owner)
    game_board.board[9].move()


def chess_string(board):
    """ Prints a Chess Board using information from the Board object."""


class Board:
    """ Initializes the game board, tracks each player's moves, and monitors the status of the chess game."""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        # Pawn initialization
        pawns1_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        p1_pawns = {}
        for name in pawns1_list:
            p1_pawns[name] = Pawn(player1)
        p2_pawns = {}
        for name in pawns1_list:
            p2_pawns[name] = Pawn(player2)
        # Rook initialization
        rooks_list = [0, 8]
        p1_rooks = []
        for name in rooks_list:
            p1_rooks.append(Rook(player1))
        p2_rooks = []
        for name in rooks_list:
            p2_rooks.append(Rook(player2))

        self.board = [(), (), (), (), (), (), (), (), ()] * 9
        for i in range(9, 18):
            self.board[i] = p1_pawns[i-9]
        for i in range(63, 72):
            self.board[i] = p2_pawns[i-63]
        # Rook Placement
        self.board[0] = p1_rooks[0]
        self.board[8] = p1_rooks[1]
        self.board[72] = p2_rooks[0]
        self.board[80] = p2_rooks[1]


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

    def move(self, location, game, click):
        if game.board[location] is type(Pawn):
            if click == location + 9:
                game.board.insert(location + 9, game.board.pop(location))
            elif click == location + 18:
                game.board.insert(location + 18, game.board.pop(location))
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

    def __move__(self):
        """

        :return:
        """
        pass


class Knight:
    """ Creates a Knight object."""


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
