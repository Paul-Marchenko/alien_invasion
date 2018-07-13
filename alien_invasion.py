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
    ship = Ship(screen)

    while True:

        game_f.check_events()
        game_f.update_screen(ai_settings, screen, ship)


run_game()