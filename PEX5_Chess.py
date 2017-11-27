#!/usr/bin/env python3
"""
This will play a game of chess through a GUI, by referencing OOP practices, developing classes for each peice type, the  and the board.

The functional requirements were determined by Cage and Christian.

Functional requirements
=======================




Object Oriented description
===========================

Player Class

The Player class represents a single player.  Some of the data in the player must be protected from
improper manipulation.  You will need to use an appropriate mix of readable/writable and read-only properties.

•	Constructor – The class’s constructor shall accept two parameters, the name of the player and the marker,
    eg, “X” or “O”.  It shall initialize all other internal variables that it will use to track wins, losses, etc.
•	name (property) – The name property shall be both readable and writable.
•	marker (property) – The marker property shall be both readable and writable but must be protected from having
    improper markers being set.  If a marker is set that is longer than one character, only the first character
    shall be saved as the marker.  If a marker is set to None or the empty string, make the marker an
    exclamation mark ‘!’ instead.
•	wins (property) – The wins property shall be read-only.
•	losses (property) – The losses property shall be read-only.
•	ties (property) – The ties property shall be read-only.
•	games_played (property) – The games_played property shall be read-only.
•	record_win (method) - This method will be called after a player has finished a game.
    It shall update internal variables as needed.
•	record_loss (method) - This method will be called after a player has finished a game.
    It shall update internal variables as needed.
•	record_tie (method) - This method will be called after a player has finished a game.
    It shall update internal variables as needed.
•	__str__ (method) – This method shall return a string representation of the player in this exact format:

        Name: marker, # wins, # losses, # ties

        For example a player named Alice using ‘X’ as her marker with 1 win, 3 losses, and 5 ties:

        Alice: X, 1 wins, 3 losses, 5 ties


TicTacToe Class

The TicTacToe class represents a single game.  Some of the data in the class must be protected
from improper manipulation.  You will need to use an appropriate mix of readable/writable and read-only properties.

•	Constructor – The class’s constructor shall accept two parameters, the two players.
    The first parameter of the two will be the player to go first.  It shall initialize internal variables.
•	current_player (property) – A read-only property, the player whose turn is next.  (returns a Player object)
•	players (property) – A read-only property, a tuple of the two current players, with the player
    who went first being the first in the tuple.  (returns Player objects)
•	winner (property) – A read-only property, the player who is the winner or None if there is
    no winner.  (returns a Player object)
•	loser (property) – A read-only property, the player who is the loser or None if there is
    no loser.  (returns a Player object)
•	turns_played (property) – A read-only property, the number of turns that have been played
    on the board so far (integer 0..9).
•	play_move (function) - This function shall accept two parameters, the row and column specifying
    the play.  The row and column are 1-indexed.  That is, the upper left cell of the board is
    row=1 col=1, not row=0 col=0.  This function will be called when a player is making a move. (returns nothing)
•	player_at (function) - This function shall accept two parameters, the row and column, and shall
    return the player who has marked that spot or None if no player has marked that spot yet.  The row and
    column are 1-indexed.   (returns a Player object)

The Console-Based Game
•	The console-based game shall use the Player classes to store player data.  It shall use the TicTacToe
    class to play each game.
•	The game shall take two players through a “best two out of three” contest.  Players shall alternate going first.
•	The game shall use console based input and output, ie, the input() and print() functions.
•	The game may use whatever additional functions are needed to be well-designed.  The function board_string
    is required though.
•	board_string (function) - This function shall accept one parameter, a TicTacToe object, and return a
    string representing the game board with the numbers 1-9 in place of the cells and appropriate markers in
    marked cells.  Each pair of columns shall have one space between them.  Each line shall end with a
    newline character \n.   This function shall not access any internal data structures within TicTacToe,
    such as whatever data structure represents your board.  The board_string function shall interact
    with the TicTacToe object through its public method player_at.


CS 210, Introduction to Programming
"""

__author__ = "Cage Campbell & Christian Sylvester"  # Your name. Ex: John Doe
__section__ = "M6"  # Your section. Ex: M1
__instructor__ = "Dr. Bower"  # Your instructor. Ex: Lt Col Doe
__date__ = ""  # Today's date. Ex: 25 Dec 2017
__documentation__ = """ None """  # Multiple lines OK with triple quotes


from chess_gui import ChessApp


def main():
    app = ChessApp()
    app.window.mainloop()

# Test input.

if __name__ == "__main__":
    main()
