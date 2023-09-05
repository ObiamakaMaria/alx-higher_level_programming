import sys


def is_safe(board, row, col, n):

    """
    Check if it is safe to place a queen in the given cell (row, col).

    Args:
    - board: The current state of the chessboard.
    - row: The row where the queen is to be placed.
    - col: The column where the queen is to be placed.
    - n: The size of the chessboard.

    Returns:
    - True if it is safe to place a queen, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_solution(board, n):
    """
    Print a solution in the specified format.

    Args:
    - board: The current state of the chessboard.
    - n: The size of the chessboard.
    """
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def solve_n_queens_util(board, col, n):
    """
    Solve the N Queens problem using backtracking.

    Args:
    - board: The current state of the chessboard.
    - col: The current column being considered.
    - n: The size of the chessboard.
    """
    if col == n:
        print_solution(board, n)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, n)
            board[i][col] = 0

def solve_n_queens(n):
    """
    Solve the N Queens problem and print all solutions.

    Args:
    - n: The size of the chessboard.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens_util(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_n_queens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
