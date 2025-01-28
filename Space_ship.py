import pygame

class space_ship:
    def __init__(self , image , position , size):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image , size)
        self.position = position
        self.size = size 

    def draw(self , screen):
        screen.blit(self.image , self.position)

