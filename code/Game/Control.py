from Game.Logic import *
from UI.GamePic import *

class GameController:
    def __init__(self, screen, rows, cols, num, theme):
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self.num = num
        self.theme = theme
        self.game_logic = GameLogic(self.rows, self.cols, self.num)
        self.line_sound = pygame.mixer.Sound(LINK_WAV)
        self.game_map = [[None for i in range(self.cols)] for j in range(self.rows)]
        self.score = 0
        self.is_started = False
        self.is_paused = False
        self.is_over = False
        self.selected_pos = []
        self.hint_path = []
        self.hint_time = 0
        self.countdown_start_ticks = None
        self.before_pause = None

    def get_element(self, x, y):
        return self.game_logic.map[x][y]

    def start_countdown(self):
        self.countdown_start_ticks = pygame.time.get_ticks()

    def set_path(self, path):
        self.hint_path = path
        self.hint_time = time.time()

    def remove_points(self, path):
        if not path:
            return []
        cleaned = [path[0]]
        for point in path[1:]:
            if point != cleaned[-1]:
                cleaned.append(point)
        return cleaned

    def update_map(self):
        for x in range(self.rows):
            for y in range(self.cols):
                py = x * PIC_HEIGHT + OFFSET_Y
                px = y * PIC_WIDTH + OFFSET_X
                if self.get_element(x, y) == BLANK:
                    self.game_map[x][y].hide()
                else:
                    pic = Pic(self.screen, self.get_element(x, y), px, py, self.theme)
                    if self.game_map[x][y] and self.game_map[x][y].is_chosen:
                        self.game_map[x][y] = pic
                        self.game_map[x][y].is_chosen = True
                    else:
                        self.game_map[x][y] = pic
                self.game_map[x][y].draw()

    def game_start(self):
        self.is_started = True
        self.is_paused = False
        self.game_logic.generate_map()
        self.start_countdown()

    def game_play(self, event):
        for x in range(self.rows):
            for y in range(self.cols):
                if self.game_map[x][y] and self.game_map[x][y].handle_event(event):
                    self.selected_pos.append((x, y))
                    self.game_map[x][y].select()
                    if len(self.selected_pos) == 2:
                        (x1, y1), (x2, y2)  = self.selected_pos
                        result = self.game_logic.is_link(x1, y1, x2, y2)
                        if self.get_element(x1, y1) != self.get_element(x2, y2):
                            result = [False, (-1, -1)]
                        if result[0]:
                            self.score += 10
                            self.game_logic.clear(x1, y1, x2, y2)
                            self.line_sound.play()
                        else:
                            self.game_map[x1][y1].is_chosen = False
                            self.game_map[x2][y2].is_chosen = False
                        self.selected_pos.clear()
        if self.game_logic.is_blank():
            self.is_over = True

    def game_pause(self):
        self.is_started = False
        self.is_paused = True
        self.before_pause = pygame.time.get_ticks() - self.countdown_start_ticks

    def game_resume(self):
        self.is_started = True
        self.is_paused = False
        self.countdown_start_ticks = pygame.time.get_ticks() - self.before_pause

    def game_prompt(self):
        path = self.game_logic.search_path()
        if path[0] and self.score >= 20 and path:
            self.score -= 20
            clean_path = self.remove_points(path[1])
            draw_path = [(x + 20, y + 20) for x, y in clean_path]
            self.set_path(draw_path)

    def game_reset(self):
        if self.score >= 30:
            self.score -= 30
            self.game_logic.reset()


