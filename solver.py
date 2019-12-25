
def solve(board):
    """
    Solves the given sudoku board using backtracking algorithm.
    """
    # Find empty space. If none exists, return true.
    empty = find_zero(board)
    if not empty:
        print_board(board)
        return True
    row, col = empty

    # Try all possible values in the coordinate of empty space.
    # If value is valid, recurse the 'solve' method.
    # Otherwise, reset value to 0 and try another value to recurse.
    for i in range(1, 10):
        if is_valid(row, col, i, board):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def find_zero(board):
    """
    Finds coordinate of empty space in board.
    If none exists, returns false.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
    return False

def is_valid(i, j, num, board):
    """
    :param i: row of input
    :param j: column of input
    :param num: input value
    :param board: 9x9 board representation
    :return: boolean of whether the input is valid
    """
    # Check validity of row.
    for k in range(len(board[i])):
        if (board[i][k] == num) and (k != i):
            return False

    # Check validity of column.
    for l in range(len(board)):
        if (board[l][j] == num) and (l != j):
            return False

    # Check validity of nonet.
    nonet_row = (i // 3) * 3
    nonet_col = (j // 3) * 3
    for k in range(nonet_row, nonet_row + 3):
        for l in range(nonet_col, nonet_col + 3):
            if (board[k][l] == num) and ((k, l) != (i, j)):
                return False
    return True

def print_board(board):
    """
    Prints sudoku board in terminal.
    Takes 9x9 2d list as input.
    """
    print(" ----------------------------- ")
    for i in range(len(board)):
        print("|", end="")
        for j in range(len(board[i])):
            print(" " + str(board[i][j]) + " ", end="")
            if (j + 1) % 3 == 0:
                print("|", end="")
        print("")
        if (i + 1) % 3 == 0:
            print(" ----------------------------- ")

# Sample game of Sudoku.
sample_game =  [[0, 0, 0, 2, 6, 0, 7, 0, 1],
                [6, 8, 0, 0, 7, 0, 0, 9, 0],
                [1, 9, 0, 0, 0, 4, 5, 0, 0],
                [8, 2, 0, 1, 0, 0, 0, 4, 0],
                [0, 0, 4, 6, 0, 2, 9, 0, 0],
                [0, 5, 0, 0, 0, 3, 0, 2, 8],
                [0, 0, 9, 3, 0, 0, 0, 7, 4],
                [0, 4, 0, 0, 5, 0, 0, 3, 6],
                [7, 0, 3, 0, 1, 8, 0, 0, 0]]
