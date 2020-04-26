"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
from collections import Counter

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count state occurences in flattened board
    counts = Counter([x for row in board for x in row])

    # Return "X" if odd number of empty squares
    return "X" if counts[None] % 2 == 0 else "O"

    # or, more succinct, but clearer and/or faster?
    # return "O" if [x for row in board for x in row].count(None) % 2 else "X"
    # return "O" if Counter([x for row in board for x in row])[None] % 2 else "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return set(
        [
            (i, j)
            for i, row in enumerate(board)
            for j, col in enumerate(row)
            if col == None
        ]
    )


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Make deep copy of the board
    next_board = deepcopy(board)

    # Add next move to the next board
    i, j = action
    next_board[i][j] = player(board)

    return next_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    rotated_board = list(zip(board))

    # assuming a move has been made
    for b in (board, rotated_board):

        # check rows/columns
        for line in b:
            if len(set(line)) == 1:
                return line[0]

        # check diagonals
        if len(set([b[i][i] for i in range(3)])) == 1:
            return b[i][i]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
