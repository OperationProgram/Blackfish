import pygame


class Door(object):
        
    def __init__(self, xPos, yPos):

        TILE_SIZE = 64
        # self.door_ID = id
        self.door = pygame.image.load('art/tiles/crate.png')
        self.rect = pygame.Rect(xPos * TILE_SIZE, yPos * TILE_SIZE, TILE_SIZE, TILE_SIZE)

        
class Box(object):
    pass


class Crate(object):
    pass    
