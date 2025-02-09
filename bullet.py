import pygame

class bullet:
    def __init__(self , spaceship):
        self.width = 3
        self.height = 35
        self.x = float(spaceship.x +  spaceship.width/2)
        self.y = float(spaceship.y)
        self.speed =  -700
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # The correction parameter is to correct the alignment of the bullet with the center of the shape ship.

    def update(self , dt):
        self.rect.y += (self.speed * dt)

    def draw(self , screen):
        pygame.draw.rect(screen, (255,0,0) , self.rect) # Red Color bullets.