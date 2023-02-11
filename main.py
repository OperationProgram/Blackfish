# Simple pygame program

# Import and initialize the pygame library
import pygame
from SWorld import World
from Characters import Blackfish

# Initalize pygame.
pygame.init()

# Class Calls
world = World()
blackfish = Blackfish()


# Run until the user asks to quits.
FPS = 60
clock = pygame.time.Clock()
run = True
while run:
    # Game clock.
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    world.redrawGameWindow(world.level_0)

    blackfish.move()
    blackfish.draw()




    
    pygame.display.update()


pygame.quit()