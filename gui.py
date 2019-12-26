import pygame
import solver
import copy

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
    orig_board = copy.deepcopy(board)

    selected = False
    valued = False
    prev_val = -1
    while True:
        for event in pygame.event.get():

            # Game exit.
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Key pressed.
            elif event.type == pygame.KEYDOWN:

                # Pressed space bar which solves the sudoku game using backtracking.
                if event.key == pygame.K_SPACE:
                    if selected:
                        reset_selected_box(valued, prev_pos, prev_val)
                        selected = False
                        valued = False
                    solve_gui(board)

                # Pressed number character with box selected.
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3,
                                   pygame.K_4, pygame.K_5, pygame.K_6,
                                   pygame.K_7, pygame.K_8, pygame.K_9]:
                    if selected:
                        reset_selected_box(valued, prev_pos, prev_val)
                        valued = True
                        delay_draw(prev_pos[0] // 55, prev_pos[1] // 55, event.unicode, grey, 0)
                        prev_val = event.unicode

                # Pressing enter with a box filled in with value.
                # Value is either valid or invalid.
                elif event.key == pygame.K_RETURN:

                    # Enter only works if there is a box selected and valued.
                    if selected & valued:
                        value = int(prev_val)
                        col, row = prev_pos[0] // 55, prev_pos[1] // 55

                        # Input is valid.
                        if solver.is_valid(row, col, value, board):
                            board[row][col] = value
                            delay_draw(col, row, value, green, 200)
                            delay_draw(col, row, value, black, 0)

                        # Input is invalid.
                        else:
                            delay_draw(col, row, value, red, 200)
                            delay_draw(col, row, value, blue, 0)
                        selected = False
                        valued = False
                        prev_val = -1

            # Mouse selection.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col, row = x // 55, y // 55

                # Selected box can be changed.
                if empty_pos(x, y, orig_board):
                    if board[row][col] != 0:
                        delay_draw(col, row, board[row][col], blue, 0)
                        board[row][col] = 0
                    if selected:
                        reset_selected_box(valued, prev_pos, prev_val)
                        valued = False
                    delay_draw(col, row, "?", grey, 0)
                    selected = True
                    prev_pos = (x, y)


def reset_selected_box(valued, prev_pos, prev_val):
    """
    Resets previously selected box to 0 graphically.
    :param valued: boolean for whether the selected box has been filled.
    :param prev_pos: position of previously selected box.
    :param prev_val: value of previously selected box. null value represented by -1.
    :return: none.
    """
    prev_col, prev_row = prev_pos[0] // 55, prev_pos[1] // 55
    if valued & (prev_val != -1):
        delay_draw(prev_col, prev_row, prev_val, blue, 0)
    else:
        delay_draw(prev_col, prev_row, "?", blue, 0)


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
            delay_draw(col, row, i, black, 90)
            if solve_gui(board):
                return True
            board[row][col] = 0
            delay_draw(col, row, i, blue, 90)
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