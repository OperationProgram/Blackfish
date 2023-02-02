# Simple pygame program

# Import and initialize the pygame library
import pygame
from GridLayout import GridLayout



pygame.init()
grid = GridLayout()


blackfishX = 0
blackfishY = 0
tileSet = [   [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]]




# Run until the user asks to quit
velocity = 4
FPS = 60
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    
    
    grid.redrawGameWindow(grid.top_left)
    if keys[pygame.K_a]:
        blackfishX -= velocity
    elif keys[pygame.K_d]:
        blackfishX += velocity
    elif keys[pygame.K_w]:
        blackfishY -= velocity 
    elif keys[pygame.K_s]:
        blackfishY += velocity
    pygame.display.update()


pygame.quit()