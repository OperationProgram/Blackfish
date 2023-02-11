import pygame
# from Players import BlackFish
from Tiles import Door

world_object = None


class SWorld(object):

    def __init__(self):

        DEFAULT_GRID_WIDTH = 10
        DEFAULT_GRID_HEIGHT = 10

        self.game_display = pygame.display.set_mode((640, 640))
        self.tile_size = 64
        self.bottom_left =   [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                              [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        # self.bottom_left_doors = [Door(DEFAULT_GRID_WIDTH / 2, 0, "top"),
        #                           Door(DEFAULT_GRID_WIDTH - 1, DEFAULT_GRID_HEIGHT / 2, "right")]
        self.bottom_left_doors = {"top":   Door(DEFAULT_GRID_WIDTH / 2, 0),
                                  "right": Door(DEFAULT_GRID_WIDTH - 1, DEFAULT_GRID_HEIGHT / 2)}                                  
        
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
        
        self.bottom_right_doors = { "top":  Door(DEFAULT_GRID_WIDTH / 2, 0),
                                    "left": Door(0, DEFAULT_GRID_HEIGHT / 2)
                                  }
        
        self.top_left  =    [[2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                             [2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
        
        self.top_left_doors = { "right": Door(DEFAULT_GRID_WIDTH - 1, DEFAULT_GRID_HEIGHT / 2),
                                "bot"  : Door(DEFAULT_GRID_WIDTH / 2, DEFAULT_GRID_HEIGHT - 1)
                              }



        self.top_right  =    [[0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
                             [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
        
        self.top_right_doors = { "bot":  Door(DEFAULT_GRID_WIDTH / 2, DEFAULT_GRID_HEIGHT - 1),
                                 "left": Door(0, DEFAULT_GRID_HEIGHT / 2)
                               }
        
        
        
    def get_world():
        global world_object
    
        if world_object is None:
            world_object = SWorld()

        return world_object
        

class TileSet(object):
    
    def __init__(self, grid, **doors):
        

        self.world = SWorld.get_world()
        self.grid = grid
        self.doors = doors
        self.world = SWorld.get_world()
        print(doors)
        self.brick = pygame.image.load('art/tiles/brick.png')
        
        self.grass = pygame.image.load(('art/tiles/grass.png'))

        self.active = False
        self.tile_size = 64
    

    def at_door(self, obj):
        for direction, door in self.doors.items():
            if (pygame.Rect.colliderect(door.rect, obj.rect)):
                return direction
            

    def drawTileSet(self):

        startX, startY = 0, 0
        for row in self.grid:
            for square in row:

                if square == 0:
                    self.world.game_display.blit(self.grass, (startX, startY))

                elif square == 1:
                    self.world.game_display.blit(self.brick, (startX, startY))
                
                elif square == 2:
                    self.world.game_display.blit(self.brick, (startX, startY))

                startX += self.tile_size

            startY += self.tile_size
            startX = 0

    
                    

if __name__ == "__main__":
    ppl = { "bob": 7,
            "steve": 9}
    
    def printDict(**kwargs):
        print(kwargs["bob"])

    printDict(**ppl)