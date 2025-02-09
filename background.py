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
    def update_screen(self , alienImage , alienHeight , alienWidth):
        curr_alien = AlienShip(self , alienImage , alienWidth , alienHeight )
        self.aliens.append(curr_alien)

    def move_aliens(self , dt):
        for alien in self.aliens:
            # print(alien.x , alien.y)
            alien.move(dt)
            if alien.y > self.screen_size[1]:
                self.aliens.remove(alien)


    def draw_aliens(self):
        for alien in self.aliens:
            alien.draw()

    def collide(self , alien , bullet):
         if (bullet.rect.x >= alien.x) and (bullet.rect.x <= alien.x + alien.width):
             if (alien.y + alien.height)>=bullet.rect.y:
                 return True
         return False

    def play_gif(self , frames):
        global current_frame
        while running:
            with lock:
                current_frame = (current_frame + 1) % len(frames)  # Loop frames
            time.sleep(1 / frame_rate)  # Adjust playback speed

    def check_collision(self , bullets , frames):
        for bullet in bullets:
            for alien in self.aliens:
                if self.collide(alien , bullet):
                    self.explosion(alien , frames)
                    bullets.remove(bullet)
                    self.aliens.remove(alien)