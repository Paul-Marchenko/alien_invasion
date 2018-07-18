import sys
import pygame


def check_keydown_events(event, ship):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(1)
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            print(2)
            check_keyup_events(event, ship)

    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         sys.exit()
    #     elif event.type == pygame.KEYDOWN:
    #         if event.key == pygame.K_RIGHT:
    #             ship.moving_right = True
    #         elif event.key == pygame.K_LEFT:
    #             ship.moving_left = True
    #     elif event.type == pygame.KEYUP:
    #         if event.key == pygame.K_RIGHT:
    #             ship.moving_right = False
    #         elif event.key == pygame.K_LEFT:
    #             ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()