import pygame
import solver

pygame.init()
win = pygame.display.set_mode((495, 495))
pygame.display.set_caption("Sudoku Solver")
myfont = pygame.font.SysFont("Arial", 30)

white = (230, 230, 250)
blue = (100, 149, 237)
grey = (128, 128, 128)
green = (173, 255, 47)
black = (0, 0, 0)
red = (220, 20, 60)

win.fill(blue)


def run(board):
    init_board()
    set_board(board)
    orig_board = board.copy()

    selected = False
    valued = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve_gui(board)

                # Pressed number character with box selected.
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3,
                                   pygame.K_4, pygame.K_5, pygame.K_6,
                                   pygame.K_7, pygame.K_8, pygame.K_9]:
                    # if selected:
                    #     col, row = prev_pos[0] // 55, prev_pos[1] // 55
                    #     if (orig_board[row][col] == 0) & ():
                    #         board[row][col] = 0
                    #         delay_draw(col, row, board[row][col], blue, 0)

                    if selected:
                        if valued:
                            delay_draw(prev_pos[0] // 55, prev_pos[1] // 55, prev_val, blue, 0)
                        else:
                            delay_draw(prev_pos[0] // 55, prev_pos[1] // 55, "?", blue, 0)
                        delay_draw(prev_pos[0] // 55, prev_pos[1] // 55, event.unicode, grey, 0)
                        valued = True
                        prev_val = event.unicode

                # Pressing enter with a box filled in with value.
                # Value is either valid or invalid.
                elif event.key == pygame.K_RETURN:
                    if selected & valued:
                        value = int(prev_val)
                        col, row = prev_pos[0] // 55, prev_pos[1] // 55
                        if solver.is_valid(row, col, value, board):
                            board[row][col] = value
                            delay_draw(col, row, value, green, 200)
                            delay_draw(col, row, value, black, 0)
                        else:
                            delay_draw(col, row, value, red, 200)
                            delay_draw(col, row, value, blue, 0)
                        selected = False
                        valued = False

            # Mouse selection.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if empty_pos(x, y, board):
                    if selected:
                        if valued:
                            delay_draw(prev_pos[0] // 55, prev_pos[1] // 55, prev_val, blue, 0)
                            valued = False
                        else:
                            delay_draw(prev_pos[0] // 55, prev_pos[1] // 55, "?", blue, 0)
                    delay_draw(x // 55, y // 55, "?", grey, 0)
                    selected = True
                    prev_pos = (x, y)


def empty_pos(x, y, board):
    """
    Converts given coordinate into row, col of the game board.
    Returns true if corresponding value equals zero, and false otherwise.
    """
    col = x // 55
    row = y // 55
    if board[row][col] == 0:
        return True
    return False


def solve_gui(board):
    """
    Solves the given sudoku board using backtracking algorithm.
    Added graphic capabilities on top of solver.solve method.
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
            delay_draw(col, row, i, white, 80)
            if solve_gui(board):
                return True
            board[row][col] = 0
            delay_draw(col, row, i, blue, 80)
    return False


def delay_draw(x, y, num, color, time):
    """
    Display given character on board and pause for 'time' milliseconds.
    """
    textsurface = myfont.render(str(num), False, color)
    win.blit(textsurface, (x * 55 + 18, y * 55 + 10))
    pygame.display.flip()
    pygame.time.delay(time)


def set_board(board):
    """
    Display given values of a partially completed board.
    Values set to 0 are not displayed as they represent empty spaces.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0:
                textsurface = myfont.render(str(board[i][j]), False, white)
                win.blit(textsurface, (j*55 + 18, i*55 + 10))

    pygame.display.flip()


def init_board():
    """
    Initialize Sudoku board as 9x9 matrix.
    Initial game values are set in 'set_board' method.
    """
    for i in range(0, 496, 55):
        # Beginning of nonets are drawn with wider lines
        if (i != 0) & (i % (55 * 3) == 0):
            pygame.draw.line(win, white, (0, i), (500, i), 3)
            pygame.draw.line(win, white, (i, 0), (i, 500), 3)
        # Non-nonet lines are thinner in comparison.
        else:
            pygame.draw.line(win, white, (0, i), (500, i))
            pygame.draw.line(win, white, (i, 0), (i, 500))

    pygame.display.flip()


run(solver.sample_game)