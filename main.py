import threading

import pygame
import sys

from pygame import mixer

import background
import Space_ship
from PIL import Image


#Initializing pygame.
pygame.init()

#Initializing the mixer module.
pygame.mixer.init()

# Getting the screen size.
info = pygame.display.Info()

# Screen size
screen_width = info.current_w
screen_height = info.current_h


# Creating time variables.
last_fire = pygame.time.get_ticks()
last_time = pygame.time.get_ticks()
clock = pygame.time.Clock()
delay = 200
birth_time = 1200
dt = clock.tick(60)

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
space_ship_width = 80
space_ship_height = 150
space_ship_size = (space_ship_width , space_ship_height)
# Placing in the bottom center.
space_ship_position = [screen_width/2 - space_ship_width/2, screen_height - space_ship_height - space_ship_height/100]
obj_space_ship = Space_ship.space_ship(space_ship_image , space_ship_position , space_ship_size , obj_background.screen)

#Alien Ship:
alien_image = 'alien_ship.png'
alien_image = pygame.image.load(alien_image)
alien_width = 50
alien_height = 70
alien_image = pygame.transform.scale(alien_image, (alien_width, alien_height))


# Load background music
pygame.mixer.music.load('space_music.mp3')  # Replace with your music file
pygame.mixer.music.play(-1)  # Loop the music indefinitely
pygame.mixer.music.set_volume(0.5)
shoot_sound = pygame.mixer.Sound("laser_sound.mp3")
shoot_sound.set_volume(0.1)

# bullets:
bullets = []
fire_time = 500
prev_fire = pygame.time.get_ticks()


# score count
score = 0

def reDrawing():
    # Redrawing the background.
    obj_background.set_image()
    # Redrawing the bullets.
    obj_background.draw_bullet(bullets)
    # Redrawing the space-ship.
    obj_space_ship.draw()
    # Drawing the aliens.
    obj_background.draw_aliens()



# Game Loop:
running = True
pause = 0
while running:

    # Update the bullets positions.
    obj_background.update_bullet(dt , bullets)

    # Updating the aliens positions.
    obj_background.move_aliens(dt)

    # Creating new Aliens after regular intervals.
    current_time = pygame.time.get_ticks()
    if current_time - last_time > birth_time:
        obj_background.update_screen(alien_image , alien_width , alien_height)
        last_time = current_time

    if current_time - prev_fire > fire_time:
        obj_background.select_alien_to_fire(bullets , obj_space_ship)
        prev_fire = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Capture the keys
    keys = pygame.key.get_pressed()

    # Move the space-ship
    obj_space_ship.move(keys , obj_background , dt)

    # Fire bullets , after regular intervals when the fire button pressed.
    current_time = pygame.time.get_ticks()
    if current_time - last_fire > delay:
        obj_space_ship.fire(keys , obj_background , shoot_sound , bullets)
        last_fire = current_time

    # Updating the alien ships , and destroying the ships which have been destroyed by the space-ship fire.
    score = obj_background.check_collision(bullets , score)

    # Checking for gameOver.
    gameOver = False
    gameOver = obj_background.game_over(obj_space_ship , bullets)
    if gameOver==True:
        bullets = []
        obj_background.show_game_over(score)
        prev_fire = current_time
        last_fire = current_time
        gameOver = False
    # Redrawing everything.
    reDrawing()
    # Refresh screen
    pygame.display.flip()
    dt = clock.tick(60)/1000

pygame.quit()
sys.exit()