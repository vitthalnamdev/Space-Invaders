import pygame


class background_screen:
    def __init__(self ,_screen , image):
        self.screen = pygame.display.set_mode(_screen)
        self.image_src = image
        self.screen_size = _screen
        self.background_image = pygame.image.load(self.image_src)
        self.background_image = pygame.transform.scale(self.background_image , self.screen_size)

    def set_image(self):
        self.screen.blit(self.background_image, (0, 0))

    def set_caption(self , caption):
        pygame.display.set_caption(caption)
    
        
