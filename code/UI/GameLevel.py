from Game.constants import *

class GameLevelScreen:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.background = load_image("ow", "level.jpg", self.screen.get_size())
        self.title = font.render("请选择游戏模式与难度", True, (0, 0, 0))
        self.title_rect = self.title.get_rect(center=(400, 80))
        self.mode_buttons = []
        self.difficulty_buttons = []
        self.back_button = pygame.Rect(0, 0, 140, 50)
        self.back_button.center = (400, 500)
        self.selected_mode = None
        mode_config = [
            ("基本模式", (250, 180)),
            ("休闲模式", (550, 180))
        ]
        for text, center in mode_config:
            rect = pygame.Rect(0, 0, 180, 60)
            rect.center = center
            self.mode_buttons.append((rect, text))
        difficulty_config = [
            ("简单", (200, 300)),
            ("普通", (400, 300)),
            ("困难", (600, 300))
        ]
        for text, center in difficulty_config:
            rect = pygame.Rect(0, 0, 140, 60)
            rect.center = center
            self.difficulty_buttons.append((rect, text))

    def draw(self):
        pygame.display.set_caption("欢乐连连看 - 关卡选择")
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title, self.title_rect)
        for rect, text in self.mode_buttons:
            pygame.draw.rect(self.screen, (240, 240, 255), rect, border_radius=15)
            pygame.draw.rect(self.screen, (100, 0, 150), rect, 3, border_radius=15)
            label = self.font.render(text, True, (100, 0, 150))
            self.screen.blit(label, label.get_rect(center=rect.center))
        if self.selected_mode == "基本模式":
            for rect, text in self.difficulty_buttons:
                pygame.draw.rect(self.screen, (255, 240, 240), rect, border_radius=15)
                pygame.draw.rect(self.screen, (150, 0, 0), rect, 3, border_radius=15)
                label = self.font.render(text, True, (150, 0, 0))
                self.screen.blit(label, label.get_rect(center=rect.center))
        pygame.draw.rect(self.screen, (255, 255, 255), self.back_button, border_radius=15)
        pygame.draw.rect(self.screen, (0, 0, 0), self.back_button, 2, border_radius=15)
        back_text = self.font.render("返回", True, (0, 0, 0))
        self.screen.blit(back_text, back_text.get_rect(center=self.back_button.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.collidepoint(event.pos):
                return "main", None
            for rect, text in self.mode_buttons:
                if rect.collidepoint(event.pos):
                    self.selected_mode = text
                if self.selected_mode == "基本模式":
                    for rect, text in self.difficulty_buttons:
                        if rect.collidepoint(event.pos):
                            return "game", {
                                "mode": "基本模式",
                                "difficulty": text
                            }
                elif self.selected_mode == "休闲模式":
                    return "game", {
                        "mode": "休闲模式",
                        "difficulty": None
                    }
        return None, None
