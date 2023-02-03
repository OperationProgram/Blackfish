# Simple pygame program

# Import and initialize the pygame library
import pygame
from SGridLayout import SGridLayout
from Players import BlackFish


pygame.init()



game_display = pygame.display.set_mode((640, 640))
blackfish = pygame.image.load('art/blackfish.png')
brick = pygame.image.load('art/tiles/brick.png')
crate = pygame.image.load('art/tiles/crate.png')
grass = pygame.image.load(('art/tiles/grass.png'))

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

##### Changes only made to this function. ##################
# You can change each block to whatever image you want in the tileSet matrix above.              

def redrawGameWindow():

    startX, startY = 0, 0
    for row in tileSet:
        for square in row:

            if square == 0:
                game_display.blit(grass, (startX, startY))

            elif square == 1:
                game_display.blit(crate, (startX, startY))
            
            elif square == 2:
                game_display.blit(brick, (startX, startY))

            startX += 64

        startY += 64
        startX = 0

    game_display.blit(blackfish, (blackfishX, blackfishY))

# Set up the drawing window


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