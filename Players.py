from SGridLayout import SGridLayout
import pygame

class BlackFish(object):

    def __init__(self):
        self.gridLayout = SGridLayout.get_map()
        self.posX = 0
        self.posY = 0
        self.velocity = 4

    def get_tile(self):
        x_tile = self.posX // 64
        y_tile = self.posY // 64

        return (x_tile, y_tile)
    def draw(self):
    
        keys = pygame.key.get_pressed()

        
        self.gridLayout.game_display.blit(self.gridLayout.blackfish, (self.posX, self.posY))
        if keys[pygame.K_a]:
            self.posX -= self.velocity
        elif keys[pygame.K_d]:
            self.posX += self.velocity
        elif keys[pygame.K_w]:
            self.posY -= self.velocity 
        elif keys[pygame.K_s]:
            self.posY += self.velocity



