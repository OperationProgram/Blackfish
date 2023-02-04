from SWorld import SWorld
import pygame


class BlackFish(object):

    def __init__(self):
        self.world = SWorld.get_world()
        self.blackfish = pygame.image.load('art/blackfish.png')
        # self.rect = self.blackfish.get_rect()
        self.rect = pygame.Rect(0,0,32,32)
        self.velocity = 4


    
    def get_tile(self):
        x_tile = self.self.rect.x // 64
        y_tile = self.self.rect.y // 64

        return (x_tile, y_tile)
    def draw(self):
    
        keys = pygame.key.get_pressed()

        
        self.world.game_display.blit(self.blackfish, (self.rect.x, self.rect.y))
        if keys[pygame.K_a]:
            self.rect.x -= self.velocity
        elif keys[pygame.K_d]:
            self.rect.x += self.velocity
        elif keys[pygame.K_w]:
            self.rect.y -= self.velocity 
        elif keys[pygame.K_s]:
            self.rect.y += self.velocity



