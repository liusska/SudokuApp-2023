import sys
from grid import Grid
from button import Button
from game_utils import (
    convert_all_cells_values_in_int,
    is_any_empty_cell_in_grid,
    is_sudoku_solved,
    is_valid_number
)
from sudoku_generator import generate_start_numbers_for_sudoku


class Game:
    def __init__(self, pg, grid):
        self.pg = pg
        self.grid = grid
        self.numbers_grid = grid.grid_numbers
        self.finish_btn = Button(pg, 200, "Finish", self.finish_game)
        self.restart_btn = Button(pg, 310, "Restart", self.restart_game)
        self.new_game_btn = Button(pg, 420, "New Game", self.new_game)

    def calculate_cell_coordinates(self):
        mouse_x, mouse_y = self.pg.mouse.get_pos()
        cell_x = mouse_y // self.grid.cell_height
        cell_y = mouse_x // self.grid.cell_width
        print(cell_x, cell_y)
        return cell_x, cell_y

    def enter_number(self, event, numbers_grid):
        cell_x, cell_y = self.calculate_cell_coordinates()
        if not is_valid_number(cell_x) or not is_valid_number(cell_y):
            print(f"Not valid coordinates {cell_x} {cell_y}" )
            return
        if type(numbers_grid[cell_x][cell_y]) == str:
            numbers_grid[cell_x][cell_y] = event.unicode
            font = self.pg.font.SysFont(None, 80)
            text_surface = font.render(event.unicode, True, self.pg.Color("black"))
            self.grid.screen.blit(text_surface, (cell_x * self.grid.cell_width, cell_y * self.grid.cell_height))
        print(numbers_grid)

    def clear_number(self):
        cell_x, cell_y = self.calculate_cell_coordinates()
        if type(self.numbers_grid[cell_x][cell_y]) == str:
            self.numbers_grid[cell_x][cell_y] = ''
            font = self.pg.font.SysFont(None, 80)
            text_surface = font.render('', True, self.pg.Color("black"))
            self.grid.screen.blit(text_surface, (cell_x * self.grid.cell_width, cell_y * self.grid.cell_height))

    def make_move(self, event, numbers_grid):
        if event.type == self.pg.KEYDOWN:
            if event.key in range(self.pg.K_1, self.pg.K_9 + 1):
                self.enter_number(event, numbers_grid)
            elif event.key in range(self.pg.K_KP1, self.pg.K_KP9 + 1):
                # Number pad keys (KP1 - KP9)
                number = int(event.unicode) if event.unicode else None
                if number is not None:
                    self.enter_number(event, numbers_grid)
            elif event.key == self.pg.K_BACKSPACE:
                self.clear_number()

    def restart_game(self):
        self.numbers_grid = self.grid.grid_copy
        self.grid = Grid(self.pg, self.numbers_grid)
        print("Sudoku restarted!")
        print(self.numbers_grid)
        self.play_game()

    def new_game(self):
        self.grid.show_difficulty_options()
        print(self.grid.selected_difficulty)
        self.numbers_grid = generate_start_numbers_for_sudoku(self.grid.selected_difficulty)
        self.grid = Grid(self.pg, self.numbers_grid)
        print("New game!")
        print(self.numbers_grid)
        self.play_game()

    def finish_game(self):
        if is_any_empty_cell_in_grid(self.numbers_grid):
            text = "There are empty cells."
            self.grid.show_popup(text)
            print(text)
            return
        copy_of_current_grid_state = convert_all_cells_values_in_int(self.numbers_grid)
        if is_sudoku_solved(copy_of_current_grid_state):
            text = "Congratulations!"
            self.grid.show_popup(text)
            print(text)
            print(self.numbers_grid)
        else:
            text = "Please try again!"
            self.grid.show_popup(text)
            print(text)
            print(self.numbers_grid)
            return

    def play_game(self):
        self.grid.draw_background()
        self.grid.draw_init_numbers()
        for event in self.pg.event.get():
            if event.type == self.pg.QUIT:
                sys.exit()
            if event.type == self.pg.KEYDOWN and not self.grid.popup_active:
                self.make_move(event, self.grid.grid_numbers)
            if event.type == self.pg.MOUSEBUTTONDOWN and self.grid.popup_active:
                self.grid.close_popup()
            self.finish_btn.handle_event(event)
            self.restart_btn.handle_event(event)
            self.new_game_btn.handle_event(event)
        if self.grid.popup_active:
            self.grid.draw_popup()

        self.finish_btn.draw(self.grid.screen)
        self.restart_btn.draw(self.grid.screen)
        self.new_game_btn.draw(self.grid.screen)

        self.pg.display.flip()
