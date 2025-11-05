from Game.constants import *

class SettingsScreen:
    def __init__(self, screen, font, config):
        self.screen = screen
        self.font = font
        self.theme = "vegetable"
        self.num = 10
        self.config = config
        self.rows = self.config["ROWS"]
        self.cols = self.config["COLS"]
        self.num = self.config["PIC_NUM"]
        pygame.mixer.music.load(BGM)
        pygame.mixer.music.play(-1)
        self.background = load_image("ow", "help_bg.jpg", self.screen.get_size())
        self.music_on = True
        self.music_button = pygame.Rect(100, 100, 200, 50)
        self.theme_buttons = []
        for i in range(1, 4):
            rect = pygame.Rect(100 + (i - 1) * 150, 250, 100, 50)
            self.theme_buttons.append((rect, i))
        self.map_size = "大"
        self.size_buttons = [
            (pygame.Rect(100, 400, 80, 50), "小"),
            (pygame.Rect(200, 400, 80, 50), "中"),
            (pygame.Rect(300, 400, 80, 50), "大")
        ]
        self.back_button = pygame.Rect(350, 500, 100, 40)

    def draw(self):
        pygame.display.set_caption("欢乐连连看 - 设置")
        self.screen.blit(self.background, (0, 0))
        music_text = f"背景音乐：{'开' if self.music_on else '关'}"
        music_surf = self.font.render(music_text, True, (0, 0, 0))
        pygame.draw.rect(self.screen, (255, 255, 255), self.music_button, border_radius=10)
        pygame.draw.rect(self.screen, (0, 0, 0), self.music_button, 2, border_radius=10)
        self.screen.blit(music_surf, music_surf.get_rect(center=self.music_button.center))

        theme_title = self.font.render("选择主题：", True, (0, 0, 0))
        self.screen.blit(theme_title, (100, 200))
        for rect, theme_num in self.theme_buttons:
            color = (200, 255, 200) if self.config["THEME"] == theme_num else (255, 255, 255)
            pygame.draw.rect(self.screen, color, rect, border_radius=10)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 2, border_radius=10)
            text = self.font.render(f"主题{theme_num}", True, (0, 0, 0))
            self.screen.blit(text, text.get_rect(center=rect.center))

        size_title = self.font.render("地图大小：", True, (0, 0, 0))
        self.screen.blit(size_title, (100, 350))
        for rect, label in self.size_buttons:
            color = (255, 220, 220) if self.map_size == label else (255, 255, 255)
            pygame.draw.rect(self.screen, color, rect, border_radius=10)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 2, border_radius=10)
            text = self.font.render(label, True, (0, 0, 0))
            self.screen.blit(text, text.get_rect(center=rect.center))

        pygame.draw.rect(self.screen, (255, 255, 255), self.back_button, border_radius=10)
        pygame.draw.rect(self.screen, (0, 0, 0), self.back_button, 2, border_radius=10)
        back_text = self.font.render("返回", True, (0, 0, 0))
        self.screen.blit(back_text, back_text.get_rect(center=self.back_button.center))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.music_button.collidepoint(event.pos):
                self.music_on = not self.music_on
                if self.music_on:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            for rect, theme_num in self.theme_buttons:
                if rect.collidepoint(event.pos):
                    self.config["THEME"] = theme_num
                    if theme_num == 1:
                        self.theme = "vegetable"
                    elif theme_num == 2:
                        self.theme = "fish"
                    elif theme_num == 3:
                        self.theme = "flower"
            for rect, label in self.size_buttons:
                if rect.collidepoint(event.pos):
                    self.map_size = label
                    if label == "小":
                        self.config["ROWS"] = self.config["COLS"] = 4
                        self.config["PIC_NUM"] = 4
                    elif label == "中":
                        self.config["ROWS"] = self.config["COLS"] = 8
                        self.config["PIC_NUM"] = 8
                    elif label == "大":
                        self.config["ROWS"] = self.config["COLS"] = 10
                        self.config["PIC_NUM"] = 10
                    self.rows = self.config["ROWS"]
                    self.cols = self.config["COLS"]
                    self.num = self.config["PIC_NUM"]
            if self.back_button.collidepoint(event.pos):
                return "main"

        return None
