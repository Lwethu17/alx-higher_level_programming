#!/usr/bin/python3
"""Solves the N-queens puzzle.
Solves all possible probability solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N isto be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for c in range(len(board)):
        for d in range(len(board)):
            if board[c][d] == "Q":
                solution.append([c, d])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for d in range(col + 1, len(board)):
        board[row][d] = "x"
    # X out all backwards spots
    for d in range(col - 1, -1, -1):
        board[row][d] = "x"
    # X out all spots below
    for c in range(row + 1, len(board)):
        board[c][col] = "x"
    # X out all spots above
    for c in range(row - 1, -1, -1):
        board[c][col] = "x"
    # X out all spots diagonally down to the right
    d = col + 1
    for d in range(row + 1, len(board)):
        if d >= len(board):
            break
        board[c][d] = "x"
        d += 1
    # X out all spots diagonally up to the left
    d = col - 1
    for c in range(row - 1, -1, -1):
        if d < 0:
            break
        board[c][d]
        d -= 1
    # X out all spots diagonally up to the right
    d = col + 1
    for c in range(row - 1, -1, -1):
        if d >= len(board):
            break
        board[c][d] = "x"
        d += 1
    # X out all spots diagonally down to the left
    d = col - 1
    for c in range(row + 1, len(board)):
        if d < 0:
            break
        board[c][d] = "x"
        d -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][d] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][d] = "Q"
            xout(tmp_board, row, d)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
