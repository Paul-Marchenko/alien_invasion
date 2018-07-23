import pygame
from r_settings import RockMainSettings
from rocket import Rocket
import rock_functions as rock_funck


def launch_rocket():

    pygame.init()
    rock_settings = RockMainSettings()
    screen = pygame.display.set_mode(rock_settings.screen_width, rock_settings.screen_height)
    pygame.display.set_caption("Yo-hooo")
    rocket = Rocket(rock_settings, screen)

    while True:
        rock_funck.rock_check_events()
        rocket.update()
        rock_funck.rock_update_screen()


launch_rocket()
