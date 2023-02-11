# Simple pygame program

# Import and initialize the pygame library
import pygame
from world import World
from blackfish import Blackfish

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


    # Draw world grids.
    blackfish.update_player_pos()

    
    pygame.display.update()


pygame.quit()