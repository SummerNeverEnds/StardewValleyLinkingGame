from Game.Control import *
from Game.constants import *

class Pic:
    def __init__(self, screen, pic_type, x, y, theme):
        self.screen = screen
        self.background = load_image(theme, str(pic_type)+".png", (PIC_WIDTH, PIC_HEIGHT))
        self.line_sound = pygame.mixer.Sound(PIC_WAV)
        self.is_visible = True
        self.is_chosen = False
        self.pic_type = pic_type
        self.pos = (x, y)
        self.rect = pygame.Rect(x, y, PIC_WIDTH, PIC_HEIGHT)

    def hide(self):
        self.is_visible = False
    def select(self):
        self.is_chosen = True
        self.line_sound.play()

    def draw(self):
        if not self.is_visible:
            return
        if self.is_chosen:
            pygame.draw.rect(self.screen, (200, 160, 255), self.rect)
        self.screen.blit(self.background, self.pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False
