import pygame
import sys

from pygame import mixer

import background
import Space_ship

#Initializing pygame.
pygame.init()

#Initializing the mixer module.
pygame.mixer.init()

# Screen size
screen_width = 1000
screen_height = 700

# Creating time variables.
last_time = pygame.time.get_ticks()
delay = 250


# Creating a background object
image = 'space.jpg'
obj_background = background.background_screen([screen_width , screen_height] , image)

# Setting , background image:
obj_background.set_image()

# Setting caption:
caption = 'Space Invaders'
obj_background.set_caption(caption)


# Creating a space_ship object
space_ship_image = 'space_ship.png'
space_ship_width = 70
space_ship_height = 160
space_ship_size = (space_ship_width , space_ship_height)
# Placing in the bottom center.
space_ship_position = [screen_width/2 - space_ship_width/2, screen_height - space_ship_height - space_ship_height/100]
obj_space_ship = Space_ship.space_ship(space_ship_image , space_ship_position , space_ship_size)
obj_space_ship.draw(obj_background.screen)

# Load background music
pygame.mixer.music.load('space_music.mp3')  # Replace with your music file
pygame.mixer.music.play(-1)  # Loop the music indefinitely
pygame.mixer.music.set_volume(0.5)
shoot_sound = pygame.mixer.Sound("laser_sound.mp3")
shoot_sound.set_volume(0.1)

# Game Loop:
running = True
pause = 0
while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    # Capture the keys
    keys = pygame.key.get_pressed()

    # Move the space-ship
    obj_space_ship.move(keys , obj_background)

    # Fire bullets , after regular intervals when the fire button pressed.
    if current_time - last_time > delay:
        obj_space_ship.fire(keys , obj_background , shoot_sound)
        last_time = current_time
    else:
        obj_space_ship.update_bullet(obj_background.screen)


    # Refresh screen
    pygame.display.flip()

pygame.quit()
sys.exit()