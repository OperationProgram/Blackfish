# Simple pygame program

# Import and initialize the pygame library
import pygame
from SGridLayout import SGridLayout
from Players import BlackFish


pygame.init()
grid = SGridLayout()
hero = BlackFish()


# Run until the user asks to quit
FPS = 60
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    
    grid.redrawGameWindow(grid.top_left)
    hero.draw()
    
    pygame.display.update()


pygame.quit()