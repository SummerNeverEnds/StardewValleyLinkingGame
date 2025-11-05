from Game.Control import *
from Game.constants import *

class GameScreen:
    def __init__(self, screen, font, theme, rows, cols, num, mode, difficulty):
        self.screen = screen
        self.font = font
        self.control = GameController(self.screen, rows, cols, num, theme)
        self.show_image_time = None
        self.image_duration = 3
        self.showing_image = False
        self.result = None
        self.background = load_image("ow", theme + ".jpg", self.screen.get_size())
        self.over = load_image("ow", "over.jpg", (500, 500))
        self.win = load_image("ow", "win.jpg", (500, 500))
        self.mode = mode
        self.difficulty = difficulty
        if difficulty == "简单":
            self.countdown_time = 300
        elif difficulty == "普通":
            self.countdown_time = 200
        elif difficulty == "困难":
            self.countdown_time = 100
        else:
            self.countdown_time = 0
        self.remaining_time = self.countdown_time
        self.resume_button = pygame.Rect(350, 320, 100, 40)
        self.button_texts = ["开始", "暂停", "提示", "重排"]
        start_x = 660
        y = 50
        self.buttons = []
        for i, text in enumerate(self.button_texts):
            rect = pygame.Rect(0, 0, 100, 40)
            rect.topleft = (start_x, y + i * 50)
            if text == "开始":
                self.buttons.append({"rect": rect, "text": text, "enabled": True})
            else:
                self.buttons.append({"rect": rect, "text": text, "enabled": False})

    def show_image(self, result):
        self.show_image_time = time.time()
        self.showing_image = True
        self.result = result

    def save_score(self, time, score, difficulty):
        if os.path.exists(RANKING_FILE):
            with open(RANKING_FILE, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []
        data.append({
            "time": time,
            "score": score,
            "difficulty": difficulty
        })
        with open(RANKING_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def update_countdown(self):
        if self.control.is_over:
            return self.remaining_time
        if self.control.countdown_start_ticks is not None:
            elapsed_time = (pygame.time.get_ticks() - self.control.countdown_start_ticks) / 1000
            self.remaining_time = self.countdown_time - elapsed_time
            if self.remaining_time <= 0:
                self.remaining_time = 0

    def draw_countdown(self):
        self.update_countdown()
        progress_bar_width = 400
        progress_bar_height = 20
        bar_x = 50
        bar_y = 540
        pygame.draw.rect(self.screen, (255, 255, 255), (bar_x, bar_y, progress_bar_width, progress_bar_height),
                         border_radius=10)
        pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, progress_bar_width * (self.remaining_time / self.countdown_time), progress_bar_height),
                         border_radius=10)
        time_text = self.font.render(f"{self.remaining_time:.3f}秒", True, (0, 0, 0))
        self.screen.blit(time_text, (bar_x + progress_bar_width + 10, bar_y))

    def draw_line(self):
        if self.control.hint_path and time.time() - self.control.hint_time < 3:
            pygame.draw.lines(self.screen, (0, 0, 0), False, self.control.hint_path, 6)
        elif self.control.hint_path and time.time() - self.control.hint_time >= 3:
            self.control.hint_path = []

    def draw_pause(self):
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill((230, 220, 250))
        self.screen.blit(overlay, (0, 0))
        pause_font = pygame.font.SysFont(FONT_NAME, 60)
        pause_text = pause_font.render("游戏已暂停", True, (80, 0, 120))
        self.screen.blit(pause_text, pause_text.get_rect(center=(400, 250)))
        pygame.draw.rect(self.screen, (255, 255, 255), self.resume_button, border_radius=10)
        pygame.draw.rect(self.screen, (100, 0, 100), self.resume_button, 2, border_radius=10)
        resume_text = self.font.render("继续", True, (100, 0, 100))
        self.screen.blit(resume_text, resume_text.get_rect(center=self.resume_button.center))

    def draw(self):
        pygame.display.set_caption("欢乐连连看 - 游戏界面")
        self.screen.blit(self.background, (0, 0))
        for button in self.buttons:
            rect = button["rect"]
            text = button["text"]
            pygame.draw.rect(self.screen, (255, 255, 255), rect, border_radius=10)
            pygame.draw.rect(self.screen, (100, 0, 100), rect, 2, border_radius=10)
            txt_surf = self.font.render(text, True, (100, 0, 100))
            txt_rect = txt_surf.get_rect(center=rect.center)
            self.screen.blit(txt_surf, txt_rect)
        score_text = self.font.render(f"当前得分: {self.control.score}", True, (80, 0, 100))
        text_rect = score_text.get_rect()
        self.screen.blit(score_text, (WIDTH - text_rect.width - 50, HEIGHT - text_rect.height - 40))
        if self.mode == "基本模式":
            self.draw_countdown()
        if self.control.is_started:
            self.control.update_map()
            if self.mode == "基本模式" and self.remaining_time <= 0 and not self.control.is_over:
                self.control.is_over = True
                self.show_image("over")
            if self.control.is_over and not self.showing_image:
                self.show_image("win")
            if self.showing_image:
                if time.time() - self.show_image_time <= self.image_duration:
                    if self.result == "over":
                        self.screen.blit(self.over, self.over.get_rect(center=(WIDTH / 2, HEIGHT / 2)))
                    elif self.result == "win":
                        self.screen.blit(self.win, self.win.get_rect(center=(WIDTH / 2, HEIGHT / 2)))
                else:
                    if self.mode == "基本模式" and self.result == "win":
                        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        score = self.control.score + int(self.remaining_time)
                        if self.difficulty == "困难":
                            score *= 3
                        elif self.difficulty == "普通":
                            score *= 2
                        self.save_score(current_time, score, self.difficulty)
                    self.showing_image = False
                    self.result = None
                    return "main"
            self.draw_line()
        if self.control.is_paused:
            self.draw_pause()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                rect = button["rect"]
                text = button["text"]
                enabled = button["enabled"]
                if self.control.is_paused and self.resume_button.collidepoint(event.pos):
                    self.control.game_resume()
                    for b in self.buttons:
                        b["enabled"] = True
                        if b["text"] == "开始":
                            b["enabled"] = False
                if rect.collidepoint(event.pos) and enabled:
                    if text == "开始":
                        self.control.game_start()
                        for b in self.buttons:
                            if b["text"] == "开始":
                                b["enabled"] = False
                            else:
                                b["enabled"] = True
                    elif text == "暂停":
                        self.control.game_pause()
                        for b in self.buttons:
                            if b["text"] != "暂停":
                                b["enabled"] = False
                    elif text == "提示":
                        self.control.game_prompt()
                    elif text == "重排":
                        self.control.game_reset()
            if self.control.is_started and not self.control.is_paused:
                self.control.game_play(event)
