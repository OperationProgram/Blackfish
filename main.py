# Simple pygame program

# Import and initialize the pygame library
import pygame


pygame.init()


game_display = pygame.display.set_mode((800, 600))
blackfish = pygame.image.load('art/blackfish.png')
bg = pygame.image.load('art/tiles/brick.png')
crate = pygame.image.load('art/tiles/crate.png')
grass = pygame.image.load(('art/tiles/grass.png'))

blackfishX = 0
blackfishY = 0
tileSet = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
def redrawGameWindow():
# COMMENTS

    game_display.blit(blackfish, (blackfishX, blackfishY))
    game_display.blit(bg, (100, 100))




    gameBoard1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def drawOnLayer():
    startX, startY = 0, 0
    for i in tileSet:
        if i == 0:
            game_display.blit(grass,(startX, startY))


# Set up the drawing window



# Run until the user asks to quit
velocity = 4
FPS = 60 ##TESTr 222
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
    drawOnLayer()
    if keys[pygame.K_a]:
        blackfishX -= velocity
    elif keys[pygame.K_d]:
        blackfishX += velocity
    elif keys[pygame.K_w]:
        blackfishY -= velocity
    elif keys[pygame.K_s]:
        blackfishY += velocity
    pygame.display.update()

# Done! Time to quit.
pygame.quit()