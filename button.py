class Button:
    def __init__(self, pg, x, text, action):
        self.pg = pg
        self.rect = pg.Rect(x, 762, 100, 30)
        self.color = pg.Color(224, 224, 224)
        self.hover_color = pg.Color(255, 255, 255)
        self.text = text
        self.text_color = pg.Color("black")
        self.action = action

    def draw(self, surface):
        if self.rect.collidepoint(self.pg.mouse.get_pos()):
            self.pg.draw.rect(surface, self.hover_color, self.rect)
        else:
            self.pg.draw.rect(surface, self.color, self.rect)

        font_btn = self.pg.font.Font(None, 24)
        text_surface = font_btn.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == self.pg.MOUSEBUTTONDOWN:
            # Left mouse button
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return self.action()
