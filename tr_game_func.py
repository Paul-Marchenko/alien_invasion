import pygame
import sys


def tr_check_events():

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()


def tr_update_status(tr_settings, tr_screen, fighter):
    tr_screen.fill(tr_settings.tr_bg_colour)
    fighter.tr_blitme()
    pygame.display.flip()