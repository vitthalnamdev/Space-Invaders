import pygame

import background
import bullet
from bullet import bullet



class space_ship():
    def __init__(self , image , position , _size , _screen):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,_size)
        self.width = _size[0]
        self.height = _size[1]
        self.screen = _screen
        self.x, self.y = float(position[0]), float(position[1])  # Use float for smooth movement
        self.vel_x = 500 # Velocity
        self.size = _size

    def draw(self):
        self.screen.blit(self.image , (self.x, self.y))


    def move(self , key , obj_background, dt):
        if key[pygame.K_LEFT]:
             self.x -= (self.vel_x*dt)
             self.x = max(0.0 , self.x)
        elif key[pygame.K_RIGHT]:
            self.x += (self.vel_x*dt)
            self.x = min(self.x , obj_background.screen_size[0] - self.size[0])


    def fire(self , key , obj_background , shoot_sound , bullets):
        if key[pygame.K_SPACE]:
            bullets.append(bullet(self))
            shoot_sound.play()




