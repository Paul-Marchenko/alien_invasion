import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as game_f
from pygame.sprite import Group
#from alien import Alien
from game_stats import GameStats
from button import Button


def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # pygame.mouse.set_visible(ai_settings.mouse_enabled)
    # pygame.key.get_focused()
    ship = Ship(ai_settings, screen)
    bullets = Group()
    #alien = Alien(ai_settings, screen)
    aliens = Group()
    game_f.create_fleet(ai_settings, screen, ship, aliens)


    while True:
        game_f.check_events(ai_settings, screen, stats, sb, play_button, ship,
           aliens, bullets)
        if stats.game_active:
            ship.update()
            game_f.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            game_f.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
               bullets)
            print(len(bullets))

            game_f.update_screen(ai_settings, screen, stats, sb, ship,
                         aliens, bullets, play_button)


run_game()

# if __name__ == '__main__':
#     run_game()
