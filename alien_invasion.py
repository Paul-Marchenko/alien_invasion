import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as game_f
from pygame.sprite import Group


def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # pygame.mouse.set_visible(ai_settings.mouse_enabled)
    # pygame.key.get_focused()
    ship = Ship(ai_settings, screen)
    bullets = Group()

    while True:
        game_f.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets)

        game_f.update_screen(ai_settings, screen, ship, bullets)


run_game()

# if __name__ == '__main__':
#     run_game()
