import pygame

import background
import bullet
from bullet import bullet



class space_ship():
    def __init__(self , image , position , _size , _screen):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,_size)
        self.screen = _screen
        self.x, self.y = float(position[0]), float(position[1])  # Use float for smooth movement
        self.vel_x = 0.5 # Velocity
        self.size = _size
        self.bullets = []

    def draw(self):
        self.screen.blit(self.image , (self.x, self.y))


    def move(self , key , obj_background:background.background_screen ):
        if key[pygame.K_LEFT]:
             self.x -= self.vel_x
             self.x = max(0.0 , self.x)
        elif key[pygame.K_RIGHT]:
            self.x += self.vel_x
            self.x = min(self.x , obj_background.screen_size[0] - self.size[0])

    def update_bullet(self):
        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.y<0:
                self.bullets.remove(bullet)

    def draw_bullet(self):
        for bullet in self.bullets:
            bullet.draw(self.screen)

    def fire(self , key , obj_background , shoot_sound):
        if key[pygame.K_SPACE]:
            self.bullets.append(bullet((self.x , self.y)))
            shoot_sound.play(-1)
        else:
            shoot_sound.stop()


