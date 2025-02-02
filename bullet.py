import pygame

class bullet:
    def __init__(self , position):
        self.width = 4
        self.height = 40
        self.x = float(position[0])
        self.y = float(position[1])
        self.speed =  -40
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # The correction parameter is to correct the alignment of the bullet with the center of the shape ship.
        self.correction = 33
        self.rect.x += self.correction

    def update(self):
        self.rect.y += (self.speed * (1/60))

    def draw(self , screen):
        pygame.draw.rect(screen, (255,0,0) , self.rect) # Red Color bullets.