from Game.constants import *

class HelpScreen:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.back_rect = pygame.Rect(0, 0, 100, 40)
        self.back_rect.center = (400, 550)
        self.background = load_image("ow", "help_bg.jpg", self.screen.get_size())
        self.text_lines = [
            "欢迎来到欢乐连连看！",
            "游戏规则：点击两个相同的图块，若它们可以用3条以内的直线相连，",
            "则可消除它们。消除所有图块即可通关。",
            "",
            "游戏共有两种模式：基本模式 和 休闲模式。",
            "其中，只有基本模式可选择难度（简单 / 普通 / 困难）。",
            "基本模式有倒计时，分别为：简单300秒、普通200秒、困难100秒。",
            "休闲模式无倒计时，适合轻松游玩。",
            "",
            "游戏界面提供：开始、暂停、提示、重排 四个按钮。",
            "每局游戏初始分为 0 分，每成功消除一对图块可获得 10 分。",
            "每次使用提示会扣除 20 分，使用重排会扣除 30 分，",
            "若当前分数不足，则无法使用对应功能。",
            "",
            "通关时，剩余时间将按 1分/秒 转换为时间奖励分加到当前分数中。",
            "若为简单模式，最终得分不变；",
            "普通模式最终得分将 ×2，困难模式最终得分将 ×3。",
            "游戏结束后的分数可在排行榜中查看。",
            "",
            "休闲模式虽有加分和扣分机制，但不会上传排行榜。",
            "",
            "点击下方按钮返回主界面。"
        ]
        self.scroll_offset = 0
        self.max_scroll = max(0, len(self.text_lines) * 30 - 450)
        self.text_color = (25, 25, 112)

    def draw(self):
        pygame.display.set_caption("欢乐连连看 - 帮助")
        self.screen.blit(self.background, (0, 0))
        for i, line in enumerate(self.text_lines):
            y = 50 + i * 30 - self.scroll_offset
            if 50 <= y <= 520:
                line_surf = self.font.render(line, True, self.text_color)
                self.screen.blit(line_surf, (50, y))

        pygame.draw.rect(self.screen, (255, 255, 255), self.back_rect, border_radius=10)
        pygame.draw.rect(self.screen, (0, 0, 0), self.back_rect, 2, border_radius=10)
        back_surf = self.font.render("返回", True, (0, 0, 0))
        back_txt_rect = back_surf.get_rect(center=self.back_rect.center)
        self.screen.blit(back_surf, back_txt_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_rect.collidepoint(event.pos):
                return "main"
            elif event.button == 4:
                self.scroll_offset = max(0, self.scroll_offset - 30)
            elif event.button == 5:
                self.scroll_offset = min(self.max_scroll, self.scroll_offset + 30)
        return None
