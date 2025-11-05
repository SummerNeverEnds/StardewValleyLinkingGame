from UI.Help import *
from UI.GameLevel import *
from UI.Game import *
from UI.Menu import *
from UI.Ranking import RankingScreen
from UI.Settings import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
current_page = "main"
main_menu_screen = MainMenuScreen(screen,font)
help_screen = HelpScreen(screen, font)
game_level_screen = GameLevelScreen(screen, font)
game_screen = None
settings_screen = SettingsScreen(screen, font, CONFIG)
ranking_screen = RankingScreen(screen, font)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if current_page == "main":
            result = main_menu_screen.handle_main_menu_events(event)
            if result == "help":
                current_page = "help"
            elif result == "level":
                current_page = "level"
            elif result == "settings":
                current_page = "settings"
            elif result == "ranking":
                current_page = "ranking"
        elif current_page == "help":
            result = help_screen.handle_event(event)
            if result == "main":
                current_page = "main"
        elif current_page == "level":
            result, data = game_level_screen.handle_event(event)
            if result == "main":
                current_page = "main"
            elif result == "game":
                theme = settings_screen.theme
                rows = settings_screen.rows
                cols = settings_screen.cols
                num = settings_screen.num
                mode = data.get("mode")
                difficulty = data.get("difficulty")
                game_screen = GameScreen(screen, font, theme, rows, cols, num, mode, difficulty)
                current_page = "game"
        elif current_page == "game":
            result = game_screen.handle_event(event)
        elif current_page == "settings":
            result = settings_screen.handle_event(event)
            if result == "main":
                current_page = "main"
        elif current_page == "ranking":
            result = ranking_screen.handle_event(event)
            if result == "main":
                current_page = "main"

    if current_page == "main":
        main_menu_screen.draw()
    elif current_page == "help":
        help_screen.draw()
    elif current_page == "level":
        game_level_screen.draw()
    elif current_page == "game":
        result = game_screen.draw()
        if result == "main":
            current_page = "main"
    elif current_page == "settings":
        settings_screen.draw()
    elif current_page == "ranking":
        ranking_screen.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
