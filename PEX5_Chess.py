"""The TicTacToe class"""


class TicTacToe:
    """ A Tic Tac Toe game model """

    def __init__(self, player1, player2):
        """
        Initializes a new TicTacToe game.
        :param Player player1:
        :param Player player2:
        """
        self.__board = [[None for _ in range(8)] for __ in range(8)]  # type: list[list[]]
        self.__players = (player1, player2)  # type: tuple[Player]
        self.__current_player_index = 0  # type: int

    @property
    def current_player(self):
        """
        Returns the current player
        :return:
        :rtype: Player
        """
        return self.__players[self.__current_player_index]

    @property
    def players(self):
        """
        Returns a list of players for the current game.
        This is a copy of the internal list, so you do not
        have to worry about messing up the list.
        :return: list of players
        :rtype: Tuple[Player]
        """
        return tuple(self.__players)

    @property
    def turns_played(self):
        """
        Returns the number of valid turns played on this board, 0..9
        :return: number of valid turns
        :rtype: int
        """
        count = 0
        for row in self.__board:
            for person in row:
                if person is not None:
                    count += 1
        return count

    @property
    def winner(self):
        """
        Returns the winner of a game or None if the game is
        not yet over or there is a tie.
        :return:
        :rtype: Player
        """
        # Check rows
        for row in self.__board:
            if len(set(row)) == 1 and row[0] is not None:
                return row[0]

        # Check columns
        for c in range(1, 4):  # columns
            p = self.player_at(1, c)
            if self.player_at(2, c) == p and self.player_at(3, c) == p:
                return p

        # Check diagonals
        p = self.player_at(2, 2)

        # Left to right
        if self.player_at(1, 1) == p and self.player_at(3, 3) == p:
            return p

        # Right to left
        if self.player_at(1, 3) == p and self.player_at(3, 1) == p:
            return p

        return None  # No winner

    @property
    def loser(self):
        """
        Returns the loser of a game or None if the game is
        not yet over or there is a tie.
        :return:
        :rtype: Player
        """
        winner = self.winner  # Put most of the logic here
        if winner is None:
            return None

        temp = list(self.players)
        temp.remove(winner)
        return temp[0]

    def play_move(self, row, col):
        row_index = row - 1
        col_index = col - 1

        self.__board[row_index][col_index] = self.current_player
        self.__current_player_index = (self.__current_player_index + 1) % 2

    def player_at(self, row, col):
        row_index = row - 1
        col_index = col - 1
        return self.__board[row_index][col_index]
