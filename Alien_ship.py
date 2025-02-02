import pygame
import numpy as np

class AlienShip:
    def __init__(self , background):
        self.screen = background.screen
        self.width = 50
        self.height = 70
        self.image = pygame.image.load('alien_ship.png')
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.y = 0
        self.x = np.random.uniform(low = self.width , high = background.screen_size[0] - self.width)
        self.speed = 7

    def move(self):
        self.y += (self.speed*(1/60))

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
