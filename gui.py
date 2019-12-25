import pygame
import solver

pygame.init()
win = pygame.display.set_mode((495, 495))
pygame.display.set_caption("Sudoku Solver")
myfont = pygame.font.SysFont("Arial", 30)

white = (230, 230, 250)
blue = (25, 25, 112)

win.fill(blue)

def run(board):
    init_board()
    set_board(board)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve_gui(board)

def solve_gui(board):
    """
    Solves the given sudoku board using backtracking algorithm.
    """
    # Find empty space. If none exists, return true.
    empty = solver.find_zero(board)
    if not empty:
        return True
    row, col = empty

    # Try all possible values in the coordinate of empty space.
    # If value is valid, recurse the 'solve' method.
    # Otherwise, reset value to 0 and try another value to recurse.
    for i in range(1, 10):
        if solver.is_valid(row, col, i, board):
            board[row][col] = i
            delay_draw(col, row, i, white)
            if solve_gui(board):
                return True
            board[row][col] = 0
            delay_draw(col, row, i, blue)
    return False

def delay_draw(x, y, num, color):
    textsurface = myfont.render(str(num), False, color)
    win.blit(textsurface, (x * 55 + 18, y * 55 + 10))
    pygame.display.flip()
    pygame.time.delay(80)

def set_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                textsurface = myfont.render(str(board[i][j]), False, white)
                win.blit(textsurface, (j*55 + 18, i*55 + 10))

    pygame.display.flip()

def init_board():
    for i in range(0, 496, 55):
        if (i != 0) & (i % (55 * 3) == 0):
            pygame.draw.line(win, white, (0, i), (500, i), 3)
            pygame.draw.line(win, white, (i, 0), (i, 500), 3)
        else:
            pygame.draw.line(win, white, (0, i), (500, i))
            pygame.draw.line(win, white, (i, 0), (i, 500))

    pygame.display.flip()

run(solver.sample_game)