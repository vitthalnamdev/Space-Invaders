import pygame
import sys
import background
import Space_ship

pygame.init()

# Screen size
screen_width = 1000
screen_height = 700

# Creating a background object
obj_background = background.background_screen((screen_width , screen_height))

# Setting , background image:
image = 'space.jpg'
obj_background.set_image(image)

# Setting caption:
caption = 'Space Invaders'
obj_background.set_caption(caption)


# Creating a space_ship object
space_ship_image = 'space_ship.png'
space_ship_width = 70
space_ship_height = 160
space_ship_size = (space_ship_width , space_ship_height)
# Placing in the bottom center.
space_ship_position = (screen_width/2 - space_ship_width/2, screen_height - space_ship_height - space_ship_height/10)
obj_space_ship = Space_ship.space_ship(space_ship_image , space_ship_position , space_ship_size)
obj_space_ship.draw(obj_background.screen)

# Game Loop:
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    pygame.display.flip()

pygame.quit()
sys.exit()