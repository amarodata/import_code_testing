"""This module plays tic-tac-toe against you in the terminal. The directory name is misleading."""

BOARD = [" "]*9

def print_board():
    """Draw the noughts and crosses grid."""
    for r in range(3):
        print(" | ".join(BOARD[r*3:r*3+3]))

def winner():
    """Return "X" or "O" if someone has three in a row."""
    raise NotImplementedError
