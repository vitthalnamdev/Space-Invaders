import pygame


class background_screen:
    def __init__(self ,_screen):
        self.screen = pygame.display.set_mode(_screen)
        self.screen_size = _screen
         
    def set_image(self , image):
        background_image = pygame.image.load(image)
        background_image = pygame.transform.scale(background_image , self.screen_size)
        self.screen.blit(background_image, (0, 0))
    
    def set_caption(self , caption):
        pygame.display.set_caption(caption)
        
