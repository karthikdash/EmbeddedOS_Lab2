# lab 2 - Week 2
# Created by Chirag Wadhwani(cw844) and Karthik D.(kd453)
# This program is a combination of two_button.py and two_collide.py

import pygame
from  pygame.locals import*
import os
from pygame import*
import time
import RPi.GPIO as gpio
import sys

os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()

def playVideo():
        ballrect = ballrect.move(speed)
        ballrect1 = ballrect1.move(speed1)
        
	if ballrect.left <0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed [1] = -speed[1]
	ballrect = ballrect.move(speed)

	if ballrect1.left <0 or ballrect1.right > width:
		speed1[0] = -speed1[0]
	if ballrect1.top < 0 or ballrect1.bottom > height:
		speed1[1] = -speed1[1]
	#if time.time() - cur > 5:

        if ballrect1.colliderect(ballrect):
            speed[0] = -speed[0]
            speed[1] = -speed[1]
            speed1[0] = -speed1[0]
            speed1[1] = -speed1[1]
	screen.fill(black)
	screen.blit(ball, ballrect)
	screen.blit(ball1, ballrect1)
	pygame.display.flip()
	if not gpio.input(27):
		pygame.quit()
		sys.exit(0)

# Setting up GPIO for exit button
gpio.setmode(gpio.BCM)
quitpin = gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)


pygame.mouse.set_visible(False)
WHITE = 255, 255, 255
BLACK = 0,0,0
screen = pygame.display.set_mode((320, 240))
my_font = pygame.font.Font(None, 50)
my_buttons = { 'start': (80, 180),'exit':(240,180)}
screen.fill(BLACK) # Erase the Work space
for my_text, text_pos in my_buttons.items():
    text_surface = my_font.render(my_text, True, WHITE)
    rect = text_surface.get_rect(center=text_pos)
    screen.blit(text_surface, rect)
pygame.display.flip()
cur_time = time.time()
video_started = False
init = False
while True and time.time() - cur_time < 10:
    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif(event.type is MOUSEBUTTONUP):
            # Put background on the area behind text
            screen.fill(BLACK) # Erase the Work space
            pos = pygame.mouse.get_pos()
            x,y = pos
            if y > 120:
                if x > 160:
                    print "exit pressed"
                    pygame.quit()
                    sys.exit(0)
                else:
                        video_started = True
    for my_text, text_pos in my_buttons.items():
        text_surface = my_font.render(my_text, True, WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface, rect)
        pygame.display.flip()
	
    if video_started:
        if not init:
            init = True
            size = width, height = 320, 240
            speed = [1,1]
            speed1 = [1,1]
            black = 0,0,0
            # screen = pygame.display.set_mode(size)
            ball = pygame.image.load("boy.png")
            ball1 = pygame.image.load("catgirl.png")
            ballrect = ball.get_rect()
            ballrect1 = ball1.get_rect()

	ballrect = ballrect.move(speed)
        ballrect1 = ballrect1.move(speed1)
        
	if ballrect.left <0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed [1] = -speed[1]
	ballrect = ballrect.move(speed)

	if ballrect1.left <0 or ballrect1.right > width:
		speed1[0] = -speed1[0]
	if ballrect1.top < 0 or ballrect1.bottom > height:
		speed1[1] = -speed1[1]
	#if time.time() - cur > 5:

        if time.time() - cur_time > 3:
            if ballrect1.colliderect(ballrect):
                speed[0] = -speed[0]
                speed[1] = -speed[1]
                speed1[0] = -speed1[0]
                speed1[1] = -speed1[1]
	screen.fill(black)
	screen.blit(ball, ballrect)
	screen.blit(ball1, ballrect1)
	pygame.display.flip()
	if not gpio.input(27):
		pygame.quit()
		sys.exit(0)


	
                


    if not gpio.input(27):
        pygame.quit()
        sys.exit(0)

pygame.quit()
