# lab 2 - Week 1
# Created by Chirag Wadhwani(cw844) and Karthik D.(kd453)
# Uses the same conect as bounce.py, but this time, it uses 2 image objects and if collision is detected between the two objects, it changes speed and direction

import os
import time

os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()

size = width, height = 320, 240
speed = [2,2]
speed1 = [2,2]
black = 0,0,0


screen = pygame.display.set_mode(size)
ball = pygame.image.load("cat.png")
ball1 = pygame.image.load("catgirl.png")
ballrect = ball.get_rect()
ballrect1 = ball1.get_rect()
cur = time.time()
while True:
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
	if time.time() - cur > 5:
            if ballrect1.colliderect(ballrect):
                speed[0] = -speed[0]
                speed[1] = -speed[1]
                speed1[0] = -speed1[0]
                speed1[1] = -speed1[1]
	screen.fill(black)
	screen.blit(ball, ballrect)
	screen.blit(ball1, ballrect1)
	pygame.display.flip()
	
