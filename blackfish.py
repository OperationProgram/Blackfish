from world import World
import pygame

class Blackfish():

    def __init__(self):
        # Map Singleton
        self.worldLayout = World.get_map()

        # Graphics
        self.blackfish_image = pygame.image.load('art/characters/standing.png')              # Main character picture.
        self.flip_blackfish = pygame.transform.flip(self.blackfish_image, True, False)
        self.scale_blackfish = pygame.transform.scale(self.blackfish_image, (64, 64))

        # Movement Animations & Images.
        self.standing = pygame.image.load('art/characters/standing.png')
        self.walkLeft = pygame.image.load('art/characters/walkRight_0.png')
        self.walkRight = []
        self.walkUp = []
        self.walkDown = []

        # Movement
        self.posX = 0
        self.posY = 0
        self.velocity = 4
        self.rect = self.blackfish_image.get_rect()
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

    def resizeImage(self, image):
        return self.worldLayout.game_display.blit(self.walkLeft, (self.posX, self.posY))

    def draw(self):

        if self.isMoving:
            if self.moveRight:
                self.worldLayout.game_display.blit(self.blackfish_image, (self.posX, self.posY))
                self.moveRight = True

            elif self.moveLeft:
                self.worldLayout.game_display.blit(self.walkLeft, (self.posX, self.posY))
                self.moveLeft = True

            elif self.moveUp:
                self.worldLayout.game_display.blit(self.blackfish_image, (self.posX, self.posY))

            elif self.moveDown:


                self.worldLayout.game_display.blit(self.blackfish_image, (self.posX, self.posY))

        else:
            self.isMoving = False

            # Standing
            self.worldLayout.game_display.blit(pygame.transform.scale(self.walkLeft, (64, 64)), (self.posX, self.posY))





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


