import pygame

import bullet

from Alien_ship import AlienShip
import random
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

    def update_bullet(self , dt , bullets):
        for bullet in bullets:
            bullet.update(dt)
            if bullet.rect.y<-20 or bullet.rect.y>(self.screen_size[1]):
                bullets.remove(bullet)

    def draw_bullet(self , bullets):
        for bullet in bullets:
            bullet.draw(self.screen)

    def find(self,spaceship):
        mn = 1e9
        index = -1
        cnt = 0
        for alien in self.aliens:
            curr = min(abs(alien.y - spaceship.y) , abs(alien.x - spaceship.x))
            if curr < mn:
                index = cnt
            cnt = cnt + 1
        return index

    def select_alien_to_fire(self , bullets , spaceship):
       if (len(self.aliens) == 0):
           return
       index = self.find(spaceship)
       curr_alien = self.aliens[index]
       BULLET =  bullet.alien_bullet(curr_alien , 500 , 4 , 25)
       bullets.append(BULLET)

    def draw_aliens(self):
        for alien in self.aliens:
            alien.draw()

    def collide(self , alien , Bullet):
         if isinstance(Bullet , bullet.alien_bullet):
             return False
         if (Bullet.rect.x >= alien.x) and (Bullet.rect.x <= alien.x + alien.width):
             if (alien.y + alien.height)>=Bullet.rect.y:
                 return True
         return False


    def check_collision(self , bullets ):
        for bullet in bullets:
            for alien in self.aliens:
                if self.collide(alien , bullet):
                    self.aliens.remove(alien)

    def safe(self , alien , spaceship):
        if alien.x > spaceship.x and alien.x < spaceship.x + spaceship.width:
            if alien.y > spaceship.y:
                return False
        return True

    def game_over(self , spaceship , bullets):
        # Checking for aliens:
        for alien in self.aliens:
            if (self.safe(alien , spaceship)==False):
                return True

        return False

    def draw_text(self , text, color, x, y):
        FONT = pygame.font.Font(None, 50)
        rendered_text = FONT.render(text, True, color)
        text_rect = rendered_text.get_rect(center=(x, y))
        self.screen.blit(rendered_text, text_rect)


    def show_game_over(self):
        while True:
            WHITE, BLACK, RED = (255, 255, 255), (0, 0, 0), (200, 0, 0)
            self.draw_text("GAME OVER", RED, self.screen_size[0]// 2, self.screen_size[1] // 3)
            self.draw_text("Press R to Restart", WHITE, self.screen_size[0] // 2, self.screen_size[1] // 2)
            self.draw_text("Press Q to Quit", WHITE, self.screen_size[0] // 2, self.screen_size[1] // 1.5)

            pygame.display.flip()

            # Handle user input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.aliens = []    # Restart the game

                        return  # Exit function and restart game loop
                    elif event.key == pygame.K_q:  # Quit game
                        pygame.quit()
                        exit()