""" Class Grid is responsible for the creation of the board for sudoku game"""

import copy
import sys
from button import Button


class Grid:
    def __init__(self, pg, start_numbers):
        self.pg = pg
        self.grid_numbers = start_numbers
        self.grid_copy = copy.deepcopy(start_numbers)
        self.font = self.pg.font.SysFont(None, 80)
        self.length = 9
        self.cell_size = 80
        self.offset_row = 58
        self.offset_col = 65
        self.screen_width = 800
        self.screen_height = 800
        self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
        self.cell_width = self.screen_width // 9
        self.cell_height = self.screen_height // 9
        self.selected_difficulty = None

        # Popup message variables
        self.popup_active = False
        self.popup_text = ""
        self.popup_font = pg.font.SysFont(None, 40)
        self.popup_rect = pg.Rect(200, 300, 400, 200)
        self.popup_color = pg.Color(255, 255, 255)
        self.popup_text_color = pg.Color(32, 32, 32)
        self.popup_close_button = pg.Rect(380, 420, 50, 50)

    def draw_background(self):
        """Draw 9x9 grid with empty cells"""
        self.screen.fill(self.pg.Color("white"))
        self.pg.draw.rect(self.screen, self.pg.Color("black"), self.pg.Rect(40, 40, 720, 720), width=6)

        for line_i in range(self.length):
            line_width = 1 if line_i % 3 > 0 else 3
            self.pg.draw.line(
                self.screen,
                self.pg.Color("black"),
                self.pg.Vector2((40 + line_i * self.cell_size), 40),
                self.pg.Vector2((40 + line_i * self.cell_size), 760),
                line_width)
            self.pg.draw.line(
                self.screen,
                self.pg.Color("black"),
                self.pg.Vector2(40, (40 + line_i * self.cell_size)),
                self.pg.Vector2(760, (40 + line_i * self.cell_size)),
                line_width)

    def draw_init_numbers(self):
        """Visualize in the grid start numbers for sudoku"""
        for row in range(self.length):
            for col in range(self.length):
                output = self.grid_numbers[row][col]
                n_text = self.font.render(str(output), True, self.pg.Color(64, 64, 64))
                self.screen.blit(
                    n_text,
                    self.pg.Vector2(
                        (col * self.cell_size) + self.offset_col,
                        (row * self.cell_size) + self.offset_row)
                )

    def show_popup(self, text):
        """Show popup window with custom information message"""
        self.popup_active = True
        self.popup_text = text

    def close_popup(self):
        """Close popup window"""
        self.popup_active = False

    def show_difficulty_options(self):
        """
        Visualize window with 3 buttons for different levels of sudoku
        difficulty: Easy, Medium and Hard
        Selected level is attached to the current object
        """
        option_buttons = [
            Button(self.pg, 0, "Easy", lambda: self.set_selected_difficulty("easy")),
            Button(self.pg, 0, "Medium", lambda: self.set_selected_difficulty("medium")),
            Button(self.pg, 0, "Hard", lambda: self.set_selected_difficulty("hard")),
        ]

        selected_difficulty = None  # Variable to store the selected difficulty

        while self.selected_difficulty is None:
            self.screen.fill(self.pg.Color("white"))

            button_width = self.screen_width // 3
            button_height = 80
            start_y = (self.screen_height - len(option_buttons) * button_height) // 2

            for event in self.pg.event.get():
                if event.type == self.pg.QUIT:
                    self.pg.quit()
                    sys.exit()
                for button in option_buttons:
                    button.handle_event(event)

            for i, button in enumerate(option_buttons):
                button.rect = self.pg.Rect((self.screen_width - button_width) // 2, start_y + i * button_height,
                                           button_width, button_height)
                button.draw(self.screen)

            self.pg.display.flip()

            if selected_difficulty is not None:
                return selected_difficulty

    def set_selected_difficulty(self, difficulty):
        """ Set selected difficulty class attr"""
        self.selected_difficulty = difficulty
        return

    def draw_popup(self):
        """Draw popup message with information and close button"""
        if self.popup_active:
            # Draw popup background
            self.pg.draw.rect(self.screen, self.popup_color, self.popup_rect)

            # Draw popup text
            text_surface = self.popup_font.render(self.popup_text, True, self.popup_text_color)
            text_rect = text_surface.get_rect(center=self.popup_rect.center)
            self.screen.blit(text_surface, text_rect)

            # Draw close button
            self.pg.draw.rect(self.screen, self.popup_text_color, self.popup_close_button)
            close_text_surface = self.popup_font.render("OK", True, self.popup_color)
            close_text_rect = close_text_surface.get_rect(center=self.popup_close_button.center)
            self.screen.blit(close_text_surface, close_text_rect)