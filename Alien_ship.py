import pygame
import numpy as np



class AlienShip:
    def __init__(self , background , alien_image , alien_width , alien_height):
        self.screen = background.screen
        self.width = alien_width
        self.height = alien_height
        self.image = alien_image
        self.mask = self.image.convert_alpha()
        self.mask = pygame.mask.from_surface(self.mask)
        self.y = 0
        self.x = np.random.uniform(low = self.width , high = background.screen_size[0] - self.width)
        self.speed = 80

    def move(self , dt):
        self.y += (self.speed*dt)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))



