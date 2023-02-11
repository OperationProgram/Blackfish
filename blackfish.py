from world import World
import pygame

class Blackfish():

    def __init__(self):
        # Map Singleton
        self.worldLayout = World.get_map()

        # Graphics
        self.blackfish = pygame.image.load('art/Blackfish_v0_32x32.png')
        self.flip_blackfish = pygame.transform.flip(self.blackfish, True, False)
        self.scale_blackfish = pygame. transform. scale(self.blackfish, (222, 12))

        # Movement
        self.posX = 0
        self.posY = 0
        self.velocity = 4
        self.rect = self.blackfish.get_rect()
        self.player_rectX = self.rect[0]
        self.player_rectY = self.rect[1]

        # Movement Flags
        self.isMoving = False
        self.moveLeft = False
        self.moveRight = False
        self.moveUp = False
        self.moveDown = False


    def get_tile(self):
        x_tile = self.posX // 64
        print(self.posX)
        y_tile = self.posY // 64

        return x_tile, y_tile

    def draw(self):
        print('CODE:', self.isMoving)
        if self.isMoving:
            if self.moveRight:
                self.worldLayout.game_display.blit(self.blackfish, (self.posX, self.posY))
                self.moveRight = True

            elif self.moveLeft:

                self.moveLeft = True

            elif self.moveUp:
                self.worldLayout.game_display.blit(self.blackfish, (self.posX, self.posY))

            elif self.moveDown:
                self.worldLayout.game_display.blit(self.blackfish, (self.posX, self.posY))

        else:
            self.isMoving = False
            self.worldLayout.game_display.blit(self.blackfish, (self.posX, self.posY))


    def move(self):

        keys = pygame.key.get_pressed()

        # LEFT

        print(self.isMoving,'CDOE')
        if keys[pygame.K_a]:
            self.posX -= self.velocity
            self.isMoving = True
            self.moveLeft = True
            self.moveRight = False

        elif keys[pygame.K_d]:
            self.posX += self.velocity
            self.isMoving = True
            self.moveLeft = False
            self.moveRight = True

        # UP
        elif keys[pygame.K_w]:
            self.posY -= self.velocity
            self.isMoving = True
            self.moveUp = True
            self.moveDown = False

        # DOWN
        elif keys[pygame.K_s]:
            self.posY += self.velocity
            self.isMoving = True
            self.moveUp = False
            self.moveDown = True

        else:
            self.isMoving = False

    def update_player_pos(self):

        if self.velocity > 0:

            self.player_rect = self.blackfish.get_rect()[0]
            self.player_rectY = self.blackfish.get_rect()[1]
            self.player_rectY += 4

            print('X:', self.player_rectX, 'Y:', self.player_rectY)
   #     else:
   #         self.player_rectX = self.blackfish.get_rect()[0]
 #           self.player_rectY = self.blackfish.get_rect()[1]


