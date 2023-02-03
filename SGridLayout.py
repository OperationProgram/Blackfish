import pygame


map_object = None

class SGridLayout(object):
    
    def __init__(self):

        self.map_object = map_object
        self.game_display = pygame.display.set_mode((640, 640))
        self.blackfish = pygame.image.load('art/blackfish.png')
        self.brick = pygame.image.load('art/tiles/brick.png')
        self.crate = pygame.image.load('art/tiles/crate.png')
        self.grass = pygame.image.load(('art/tiles/grass.png'))
        self.tile_size = 64

        DEFAULT_GRID_WIDTH = 10
        DEFAULT_GRID_HEIGHT = 10

        self.bottom_left =  [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                             [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        # self.bottom_left_doorRight_upper = (DEFAULT_GRID_WIDTH - 1, self.tile_size *  DEFAULT_GRID_HEIGHT / 2)
        # self.bottom_left_doorRight_lower = (DEFAULT_GRID_WIDTH - 1, (self.tile_size * DEFAULT_GRID_HEIGHT / 2) + self.tile_size)
        # self.bottom_left_doorTop = self.bottom_left[0][DEFAULT_GRID_WIDTH / 2]
        self.bottom_left_doorRight = (DEFAULT_GRID_WIDTH - 1, DEFAULT_GRID_HEIGHT / 2)
        print(self.bottom_left_doorRight)

        self.bottom_right = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
                             [0, 0, 0, 0, 0, 0, 0, 0, 2, 2]]
        # self.bottom_right_doorLeft_upper = (0, self.tile_size * DEFAULT_GRID_HEIGHT / 2)
        # self.bottom_right_doorLeft_lower = self.bottom_left(0, (self.tile_size * DEFAULT_GRID_HEIGHT / 2) + self.tile_size)
        
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


        


    def get_map():
        global map_object
    
        if map_object is None:
            map_object = SGridLayout()

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

        

        
