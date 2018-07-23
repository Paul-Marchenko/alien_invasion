import pygame


class Fighter:
    def __init__(self, tr_screen):

        self.tr_screen = tr_screen
        self.image = pygame.image.load('images/fighter.bmp')
        self.rect = self.image.get_rect()
        self.tr_screen_rect = tr_screen.get_rect()
        self.rect.centerx = self.tr_screen_rect.centerx
        self.rect.centery = self.tr_screen_rect.centery

        # self.screen = screen
        # self.image = pygame.image.load('images/rocket.bmp')
        # self.rect = self.image.get_rect()
        # self.screen_rect = screen.get_rect()
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom

    def tr_blitme(self):
        self.tr_screen.blit(self.image, self.rect)