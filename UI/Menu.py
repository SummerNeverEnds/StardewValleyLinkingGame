from Game.constants import *

class MainMenuScreen:
    def __init__(self,screen,font):
        self.screen = screen
        self.font = font
        self.background = load_image("ow", "background.jpg", self.screen.get_size())
        self.button_texts = ["开始", "帮助", "设置", "排行榜"]
        self.buttons = []
        self.button_configs = [
            {"text": "开始", "center": (733, 431), "size": (80, 50)},
            {"text": "帮助", "center": (361, 535), "size": (60, 30)},
            {"text": "设置", "center": (733, 491), "size": (80, 50)},
            {"text": "排行榜", "center": (733, 551), "size": (80, 50)}
        ]
        for config in self.button_configs:
            rect = pygame.Rect(0, 0, *config["size"])
            rect.center = config["center"]
            self.buttons.append((rect, config["text"]))

    def draw(self):
        pygame.display.set_caption("欢乐连连看 - 主界面")
        self.screen.blit(self.background, (0, 0))
        for rect, text in self.buttons:
            pygame.draw.rect(self.screen, (255, 255, 255), rect, border_radius=10)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 2, border_radius=10)
            txt_surf = self.font.render(text, True, (0, 0, 0))
            txt_rect = txt_surf.get_rect(center=rect.center)
            self.screen.blit(txt_surf, txt_rect)

    def handle_main_menu_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for rect, text in self.buttons:
                if rect.collidepoint(event.pos):
                    if text == "帮助":
                        return "help"
                    elif text == "开始":
                        return "level"
                    elif text == "设置":
                        return "settings"
                    elif text == "排行榜":
                        return "ranking"
        return None