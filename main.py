# Simple pygame program

# Import and initialize the pygame library
import pygame
from SGridLayout import SGridLayout
from Players import BlackFish


pygame.init()
grid = SGridLayout()
hero = BlackFish()


# Run until the user asks to quits
FPS = 60
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    
    print(hero.get_tile() )
    
    if ( hero.get_tile()[0] >= grid.bottom_left_doorRight[0]-1 and \
         hero.get_tile()[1] >= grid.bottom_left_doorRight[1]-1 and \
         hero.get_tile()[1] <= grid.bottom_left_doorRight[1]):
        
        grid.redrawGameWindow(grid.bottom_right)
        # hero.posX = 0
        # hero.posY = 0
    else:
        grid.redrawGameWindow(grid.bottom_left)    
    hero.draw()
    
    pygame.display.update()


pygame.quit()