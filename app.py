import copy
import pygame as pg
from grid import Grid
from game import Game
from sudoku_generator import generate_start_numbers_for_sudoku


if __name__ == "__main__":
    pg_obj = pg.init()
    solved_numbers = generate_start_numbers_for_sudoku()
    init_numbers = copy.deepcopy(solved_numbers)

    grid_obj = Grid(pg, init_numbers)
    game_obj = Game(pg, grid_obj)

    while True:
        game_obj.play_game()

#
# button1 = Button(
#     button_x,
#     button_y,
#     button_width, button_height, button_color, button_hover_color,
#                  "Button 1", button_text_color, button1_action)
#
# button2 = Button(
#     button_x + button_width + button_margin,
#     button_y,
#     button_width, button_height,
#                  button_color, button_hover_color, "Button 2", button_text_color, button2_action)
#
# button3 = Button(
#     button_x + 2 * (button_width + button_margin)
#     , button_y,
#     button_width, button_height,
#                  button_color, button_hover_color, "Button 3", button_text_color, button3_action)
