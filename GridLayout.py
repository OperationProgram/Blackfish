import pygame


map_object = None
class SGridLayout(object):
    
    def __init__(self):

        self.bottom_left =  [[2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                             [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.bottom_right =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
                             [0, 0, 0, 0, 0, 0, 0, 0, 2, 2]]
        
        self.top_left =     [[2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                             [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        self.top_right =    [[0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
                             [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


        self.game_display = pygame.display.set_mode((640, 640))
        self.blackfish = pygame.image.load('art/blackfish.png')
        self.brick = pygame.image.load('art/tiles/brick.png')
        self.crate = pygame.image.load('art/tiles/crate.png')
        self.grass = pygame.image.load(('art/tiles/grass.png'))


    def get_map(self):
        global map_object
    
        if map_object is None:
            map_object = ()

        return map_object

    def redrawGameWindow(self, grid):

        startX, startY = 0, 0
        for row in grid:
            for square in row:

                if square == 0:
                    self.game_display.blit(self.grass, (startX, startY))

                elif square == 1:
                    self.game_display.blit(self.crate, (startX, startY))
                
                elif square == 2:
                    self.game_display.blit(self.brick, (startX, startY))

                startX += 64

            startY += 64
            startX = 0

        # self.game_display.blit(self.blackfish, (self.blackfishX, self.blackfishY))

        
