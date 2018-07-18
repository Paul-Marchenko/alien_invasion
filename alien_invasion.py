import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as game_f


def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # pygame.mouse.set_visible(ai_settings.mouse_enabled)
    # pygame.key.get_focused()
    ship = Ship(ai_settings, screen)

    while True:
        game_f.check_events(ship)

        ship.update()
        game_f.update_screen(ai_settings, screen, ship)


run_game()

# if __name__ == '__main__':
#     run_game()
