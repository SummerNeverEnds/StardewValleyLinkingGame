from Game.constants import *

class RankingScreen:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.title_font = pygame.font.SysFont(FONT_NAME, FONT_SIZE + 10)
        self.background = load_image("ow", "help_bg.jpg", self.screen.get_size())
        self.back_rect = pygame.Rect(0, 0, 100, 40)
        self.back_rect.center = (400, 550)

    def load_rankings(self):
        if not os.path.exists(RANKING_FILE):
            return []
        with open(RANKING_FILE, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return sorted(data, key=lambda x: x["score"], reverse=True)[:10]
            except json.JSONDecodeError:
                return []

    def draw(self):
        pygame.display.set_caption("欢乐连连看 - 排行榜")
        self.screen.blit(self.background, (0, 0))
        title = self.title_font.render("排行榜 (前10)", True, (0, 0, 128))
        self.screen.blit(title, (300, 30))
        for i, record in enumerate(self.load_rankings()):
            text = f"{i+1}. {record['time']} - {record['score']} 分 ({record['difficulty']})"
            text_surf = self.font.render(text, True, (25, 25, 112))
            self.screen.blit(text_surf, (100, 100 + i * 35))
        pygame.draw.rect(self.screen, (255, 255, 255), self.back_rect, border_radius=10)
        pygame.draw.rect(self.screen, (0, 0, 0), self.back_rect, 2, border_radius=10)
        back_surf = self.font.render("返回", True, (0, 0, 0))
        back_txt_rect = back_surf.get_rect(center=self.back_rect.center)
        self.screen.blit(back_surf, back_txt_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_rect.collidepoint(event.pos):
                return "main"
        return None
