from SWorld import World
import pygame

class Blackfish():

    def __init__(self):
        # Map Singleton
        self.worldLayout = World.get_map()

        # Graphics
        self.blackfish_image = pygame.image.load('art/moveAnimations/down/walkDown_0.png')              # Main moveAnimations picture.
        self.flip_blackfish = pygame.transform.flip(self.blackfish_image, True, False)
        self.scale_blackfish = pygame.transform.scale(self.blackfish_image, (64, 64))
        self.player_scaleX = 64
        self.player_scaleY = 64

        # Movement Animations & Images.
        self.standing = pygame.image.load('art/moveAnimations/down/walkDown_0.png')
        self.walkLeft = pygame.image.load('art/moveAnimations/left/walkLeft_0.png')
        self.walkRight = pygame.image.load('art/moveAnimations/right/walkRight_0.png')
        self.walkUp = pygame.image.load('art/moveAnimations/up/walkUp_0.png')
        self.walkDown = pygame.image.load('art/moveAnimations/down/walkDown_0.png')

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


    def draw(self):

        # Currently, draws player in the moving direction, animation, and scales

        if self.isMoving:

            if self.moveLeft:
                self.worldLayout.game_display.blit(pygame.transform.scale(self.walkLeft,
                                                                          (self.player_scaleX, self.player_scaleY)), (self.posX, self.posY))

            elif self.moveRight:
                self.worldLayout.game_display.blit(pygame.transform.scale(self.walkRight,
                                                                          (self.player_scaleX, self.player_scaleY)), (self.posX, self.posY))

            elif self.moveUp:
                self.worldLayout.game_display.blit(pygame.transform.scale(self.walkUp,
                                                                          (self.player_scaleX, self.player_scaleY)),(self.posX, self.posY))

            elif self.moveDown:
                self.worldLayout.game_display.blit(pygame.transform.scale(self.walkDown,
                                                                          (self.player_scaleX, self.player_scaleY)), (self.posX, self.posY))

        else:
            self.isMoving = False

            # Standing
            self.worldLayout.game_display.blit(pygame.transform.scale(self.standing,
                                                                      (self.player_scaleX, self.player_scaleY)), (self.posX, self.posY))





    def move(self):

        keys = pygame.key.get_pressed()

        # LEFT
        if keys[pygame.K_a]:
            self.posX -= self.velocity
            self.isMoving = True
            self.moveLeft = True
            self.moveRight = False

        # RIGHT
        elif keys[pygame.K_d]:
            self.posX += self.velocity
            self.isMoving = True
            self.moveRight = True
            self.moveLeft = False


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
            self.moveDown = True
            self.moveUp = False


        else:
            self.isMoving = False
            self.moveLeft = False
            self.moveRight = False
            self.moveUp = False
            self.moveDown = False



