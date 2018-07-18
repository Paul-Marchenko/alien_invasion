import pygame
import sys
from tr_settings import Tr_Settings
from fighter import Fighter
import tr_game_func


def try_run_game():
        pygame.init()
        training_settings = Tr_Settings()
        tr_screen = pygame.display.set_mode(
            (training_settings.tr_screen_height, training_settings.tr_screen_width))
        pygame.display.set_caption("Train, please!!!")
        fighter = Fighter(tr_screen)

        while True:
            tr_game_func.tr_check_events()
            tr_game_func.tr_update_status(training_settings, tr_screen, fighter)


try_run_game()