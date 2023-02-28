# Simple pygame program

# Import and initialize the pygame library
import pygame
from SWorld import SWorld, TileSet
from Characters import Blackfish

pygame.init()
world = SWorld()

# Tilesets for each area of map
bottom_left  = TileSet(world.bottom_left, "bottom_left", **world.bottom_left_doors)
bottom_right = TileSet(world.bottom_right, "bottom_right", **world.bottom_right_doors)
top_left     = TileSet(world.top_left, "top_left", **world.top_left_doors)
top_right    = TileSet(world.top_right, "top_right", **world.top_right_doors)

WorldGraph = { 
    bottom_left   : [bottom_right, top_left],  
    top_left      : [top_right, bottom_left],
    top_right     : [bottom_right, top_left],  
    bottom_right  : [bottom_right, top_left]    
}

blackfish = Blackfish()

# Still not using graphing really. Shouldn't need this function at all. Look at line 57.
def change_tileSet(door):

    next_tileSet_name = curr_tileSet.doors[door].portal_to
    for tileSet in WorldGraph.keys():
        if tileSet.name == next_tileSet_name:
            curr_tileSet.active = False
            tileSet.active = True

            return tileSet


bottom_left.active = True
curr_tileSet = bottom_left

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

# Check for door collision
    if top_left.active:
        if top_left.at_door(blackfish) == "right":
            # curr_tileSet = curr_tileSet[top_left][0]  This actually is all you need 
            curr_tileSet = change_tileSet("right")

        if top_left.at_door(blackfish) == "bot":
            curr_tileSet = change_tileSet("bot")



    if top_right.active:
        if top_right.at_door(blackfish) == "bot":
            curr_tileSet = change_tileSet("bot")

        if top_right.at_door(blackfish) == "left":
            curr_tileSet = change_tileSet("left")



    if bottom_left.active:
        if bottom_left.at_door(blackfish) == "top":
            curr_tileSet = change_tileSet("top")

        if bottom_left.at_door(blackfish) == "right":
            curr_tileSet = change_tileSet("right")



    if bottom_right.active:
        if bottom_right.at_door(blackfish) == "top":
            curr_tileSet = change_tileSet("top")

        if bottom_right.at_door(blackfish) == "left":
            curr_tileSet = change_tileSet("left")
            # blackfish.rectX = world.bottom_left_doors[ "right"].rect.x
            # blackfish.rectY = world.bottom_left_doors[ "right"].rect.y
        
        
    # Renders
    curr_tileSet.drawTileSet()   
    blackfish.move()
    blackfish.draw()
    
    pygame.display.update()

    
pygame.quit()
