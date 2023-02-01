import pygame.display

game_display = pygame.display.set_mode((800, 600))
bg = pygame.image.load('art/brick.png')


def redrawGameWindow():
    game_display.blit(bg, (0, 0))




    pygame.display.update()