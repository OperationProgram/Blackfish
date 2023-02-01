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

def redrawGameWindow():
# COMMENTS

    game_display.blit(blackfish, (blackfishX, blackfishY))
    game_display.blit(bg, (0, 0))

    gameBoard0 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


    gameBoard1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Set up the drawing window



# Run until the user asks to quit
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
    if keys[pygame.K_LEFT]:
        blackfishX -= 1
    elif keys[pygame.K_RIGHT]:
        blackfishX += 1
    elif keys[pygame.K_UP]:
        blackfishY -= 1
    elif keys[pygame.K_DOWN]:
        blackfishY += 1
    pygame.display.update()

# Done! Time to quit.
pygame.quit()