import pygame
from world import World

class NPC():
    def __int__(self):

    def draw(self):
        self.gridLayout.game_display.blit(pygame.transform.flip(self.blackfish, True, False), (self.posX, self.posY))
        self.g