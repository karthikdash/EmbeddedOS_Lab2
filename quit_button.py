# lab 2 - Week 2
# Created by Chirag Wadhwani(cw844) and Karthik D.(kd453)
# This program has a quit button that exits to the Linux Terminal when pressed

import pygame
from  pygame.locals import*
import os
from pygame import*
import time
import RPi.GPIO as gpio
import sys

# Setting up GPIO for exit button
gpio.setmode(gpio.BCM)
quitpin = gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)

os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
pygame.init()
pygame.mouse.set_visible(False)
WHITE = 255, 255, 255
BLACK = 0,0,0
screen = pygame.display.set_mode((320, 240))
my_font = pygame.font.Font(None, 50)
my_buttons = { 'exit':(160,180)}
screen.fill(BLACK) # Erase the Work space
for my_text, text_pos in my_buttons.items():
    text_surface = my_font.render(my_text, True, WHITE)
    rect = text_surface.get_rect(center=text_pos)
    screen.blit(text_surface, rect)
pygame.display.flip()
cur_time = time.time()
while True and time.time() - cur_time < 10:
    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if y > 120:
                if x < 160:
                    print "exit pressed"
                    pygame.quit()
                    sys.exit(0)

    if not gpio.input(27):
        pygame.quit()
        sys.exit(0)

pygame.quit()
