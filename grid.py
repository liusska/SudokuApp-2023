import copy


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

    def draw_background(self):
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