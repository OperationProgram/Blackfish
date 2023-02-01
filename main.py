# Simple pygame program

# Import and initialize the pygame library
import pygame


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

##### Changes only made to this function. #################
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

    game_display.blit(crate, (0, 0))
    game_display.fill((0, 0, 0))
    
    redrawGameWindow()
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