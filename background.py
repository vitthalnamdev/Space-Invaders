import pygame
from Alien_ship import AlienShip

class background_screen:
    def __init__(self ,_screen , image):
        self.screen = pygame.display.set_mode(_screen)
        self.image_src = image
        self.screen_size = _screen
        self.background_image = pygame.image.load(self.image_src)
        self.background_image = pygame.transform.scale(self.background_image , self.screen_size)
        self.aliens = []

    def set_image(self):
        self.screen.blit(self.background_image, (0, 0))

    def set_caption(self , caption):
        pygame.display.set_caption(caption)

    # Adding alien ships to the background of the screen.
    def update_screen(self):
        self.aliens.append(AlienShip(self))

    def move_aliens(self):
        temp = []
        for alien in self.aliens:
            # print(alien.x , alien.y)
            alien.move()
            if alien.y < self.screen_size[1]:
                temp.append(alien)
        self.aliens = temp

    def draw_aliens(self):
        for alien in self.aliens:
            alien.draw()

