import pygame

class bullet:
    def __init__(self , ship , speed = -700 , width = 3 , height = 35):
        self.width = width
        self.height = height
        self.x = float(ship.x +  ship.width/2)
        self.y = float(ship.y)
        self.speed =  speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def update(self , dt):
        self.rect.y += (self.speed * dt)

    def draw(self , screen):
        pygame.draw.rect(screen, (0,255,0) , self.rect) # Red Color bullets.



class alien_bullet:
    def __init__(self, ship, speed=400, width=2, height=30):
        self.width = width
        self.height = height
        self.correctness_factor = 8.5
        self.x = float(ship.x + ship.width // 2 - self.correctness_factor)
        self.y = float(ship.y) + ship.speed
        self.speed = speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect_surface = pygame.Surface((self.rect.width, self.rect.height))
        self.mask = pygame.mask.from_surface(self.rect_surface)

    def update(self, dt):
        self.rect.y += (self.speed * dt)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Red Color bullets.