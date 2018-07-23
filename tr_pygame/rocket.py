import pygame
from r_settings import RockMainSettings

class Rocket:
    def __init__(self, rock_settings, screen):

        self.screen = screen
        self.rock_settings = rock_settings
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def rocket_update(self):
        if self.moving_right:
            self.rect.centery +=1
        if self.moving_left:
            self.rect.centery -=1
        if self.moving_up:
            self.rect.centery += 1
        if self.moving_down:
            self.rect.centery += 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)


