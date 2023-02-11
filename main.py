# Simple pygame program

# Import and initialize the pygame library
import pygame
from SWorld import SWorld, TileSet
from Characters import BlackFish

pygame.init()
world = SWorld()

# Tilesets for each area of map
top_left     = TileSet(world.top_left, **world.top_left_doors)
top_right    = TileSet(world.top_right, **world.top_right_doors)
bottom_left  = TileSet(world.bottom_left, **world.bottom_left_doors)
bottom_right = TileSet(world.bottom_right, **world.bottom_right_doors)



blackfish = BlackFish()
curr_tileSet = bottom_left
bottom_left.active = True


# Run until the user asks to quits
FPS = 60
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


############ LET THE MESS BEGIN - PLZ refactor #############################



    if top_left.active:

        if top_left.at_door(blackfish) == "right":
            curr_tileSet = top_right
            top_right.active = True
            top_left.active = False

        if top_left.at_door(blackfish) == "bot":
            curr_tileSet = bottom_left
            bottom_left.active = True
            top_left.active = False

    if top_right.active:

        if top_right.at_door(blackfish) == "bot":
            curr_tileSet = bottom_right
            bottom_right.active = True
            top_right.active = False

        if top_right.at_door(blackfish) == "left":
            curr_tileSet = top_left
            top_left.active = True
            top_right.active = False

    if bottom_left.active:

        if bottom_left.at_door(blackfish) == "top":
            curr_tileSet = top_left
            top_left.active = True
            bottom_left.active = False

        if bottom_left.at_door(blackfish) == "right":
            curr_tileSet = bottom_right
            bottom_right.active = True
            bottom_left.active = False

    if bottom_right.active:

        if bottom_right.at_door(blackfish) == "top":
            curr_tileSet = top_right
            top_right.active = True
            bottom_right.active = False

        if bottom_right.at_door(blackfish) == "left":
            curr_tileSet = bottom_left
            bottom_left.active = True
            bottom_right.active = False
            blackfish.rectX = world.bottom_left_doors[ "right"].rect.x
            blackfish.rectY = world.bottom_left_doors[ "right"].rect.y
        
        
    
    curr_tileSet.drawTileSet()   
    blackfish.draw()
    
    pygame.display.update()

    
pygame.quit()