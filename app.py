import copy
import pygame as pg
from grid import Grid
from game import Game
from sudoku_generator import generate_start_numbers_for_sudoku


if __name__ == "__main__":
    pg_obj = pg.init()
    solved_numbers = generate_start_numbers_for_sudoku('easy')
    init_numbers = copy.deepcopy(solved_numbers)

    grid_obj = Grid(pg, init_numbers)
    grid_obj.pg.display.set_caption("Sudoku")

    game_obj = Game(pg, grid_obj)

    while True:
        game_obj.play_game()