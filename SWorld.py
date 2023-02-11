import pygame


map_object = None

class World():
    
    def __init__(self):


        self.map_object = map_object
        self.game_display = pygame.display.set_mode((1024, 1024))

        self.brick = pygame.image.load('art/tiles/brick.png')
        self.crate = pygame.image.load('art/tiles/crate.png')
        self.grass = pygame.image.load(('art/tiles/grass.png'))
        self.tree = pygame.image.load('art/tiles/tree_style_one.png')

        #  **WARNING DEAD CODE** Graphics in testing.
        self.unusedArt = pygame.image.load('art/tree-model_v1.png')

        self.tile_size = 64

        self.screen_width = 800
        self.screen_height = 600

        DEFAULT_GRID_WIDTH = 20
        DEFAULT_GRID_HEIGHT = 20

        self.level_0 = [[0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 4, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 4, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 4, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0]]


        self.level_1 = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]]
        
        self.level_3 = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]]


        self.level_4 = [[2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]]




    def get_map():
        global map_object

        if map_object is None:
            map_object = World()

        return map_object

    def redrawGameWindow(self, grid):

        startX, startY = 0, 0
        for row in grid:
            for tile in row:

                if tile == 0:
                    self.game_display.blit(self.grass, (startX, startY))

                elif tile == 1:
                    self.game_display.blit(self.crate, (startX, startY))
                
                elif tile == 2:
                    self.game_display.blit(self.brick, (startX, startY))

                elif tile == 3:
                    self.game_display.blit(self.tree, (startX, startY))

                # Tile 4 is being used to test new tiles.
                elif tile == 4:
                    self.game_display.blit(self.unusedArt, (startX, startY))

                startX += 64

            startY += 64
            startX = 0

    def worldCompiler(self):
        pass


    def checkCollision(self, crash_tileX, crash_tileY):
        blackfish_coordinates = (crash_tileX, crash_tileY)
        print(blackfish_coordinates)



