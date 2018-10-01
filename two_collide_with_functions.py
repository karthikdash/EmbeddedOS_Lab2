

import pygame # Import Library and initialize pygame
import math
from pygame.locals import *
import os
import sys
import RPi.GPIO as gpio
import time
os.putenv('SDL_VIDEODRIVER', 'fbcon') # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1') 
os.putenv('SDL_MOUSEDRV', 'TSLIB') # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
gpio.setmode(gpio.BCM)

quitpin = gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)
pygame.init()

pygame.mouse.set_visible(False)


size = width, height = 320, 240
#size = width, height = 1020,1020
font_quit = pygame.font.Font(None,15)
buttons = {'start':(40,190), 'quit':(280,190)}
font_cord = pygame.font.Font(None,15)
font_buttons = pygame.font.Font(None,20)
buttons2 = { 'Pause':(40,200),'Fast':(120,200),'Slow':(200,200),'Back':(280,200)}

speed1 = [1,1]
speed2 = [1,1]
tempspeed = [0,0]
temps1 = [0,0]
temps2 = [0,0]
black = 0, 0, 0
WHITE = 255, 255, 255
screen = pygame.display.set_mode(size)
ball1 = pygame.image.load("catgirl.png")
w1,h1 = ball1.get_size()
ball1 = pygame.transform.scale(ball1,(int(w1/5),int(h1/5)))
ball2 = pygame.image.load("boy.png")
w2,h2 = ball2.get_size()
ball2 = pygame.transform.scale(ball2,(int(w2/5),int(h2/5)))
ballrect1 = ball1.get_rect()
ballrect2 = ball2.get_rect()

ballrect1.center = [60,100]
ballrect2.center = [140, 180]
radius1 = abs(ballrect1.left-ballrect1.right)/2
radius2 = abs(ballrect2.left-ballrect2.right)/2



x=0
y=0
flag = False
pflag = False


while 1:
    
    time.sleep(0.1)
    if flag == True:
        ballrect1 = ballrect1.move(speed1)
        ballrect2 = ballrect2.move(speed2)
        ballrect1.center = [(ballrect1.left+ballrect1.right)/2,(ballrect1.top+ballrect1.bottom)/2]
        ballrect2.center = [(ballrect2.left+ballrect2.right)/2,(ballrect2.top+ballrect2.bottom)/2]
        dist = math.pow((ballrect1.center[0]-ballrect2.center[0]),2)+math.pow((ballrect2.center[1]-ballrect2.center[1]),2)
        dist = math.sqrt(dist)
        if ballrect1.left <= 0 or ballrect1.right >= width:
            speed1[0] = -speed1[0]
        if ballrect1.top <= 0 or ballrect1.bottom >= height:
            speed1[1] = -speed1[1]
        if ballrect2.left <= 0 or ballrect2.right >= width:
            speed2[0] = -speed2[0]
        if ballrect2.top <= 0 or ballrect2.bottom >= height:
            speed2[1] = -speed2[1]
        if dist <= (radius1+radius2):
            tempspeed[0] = speed1[0]
            tempspeed[1] = speed1[1]
            speed1[0] = speed2[0]
            speed1[1] = speed2[1]
            speed2[0] = tempspeed[0]
            speed2[1] = tempspeed[1]


    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if flag == False:
                if y > 170 and y < 230:
                    if x >250 and x < 310:
                        sys.exit()
                    elif x>10 and x<70:
                        flag = True
            else:
                if y>170 and y<230:
                    if x >10 and x<70:
                        if pflag == False:
                            temps1[0] = speed1[0]
                            temps1[1] = speed1[1]
                            temps2[0] = speed2[0]
                            temps2[1] = speed2[1]
                            speed1[0] = 0
                            speed1[1] = 0
                            speed2[0] = 0
                            speed2[1] = 0
                            pflag = True
                        elif pflag == True:
                            speed1[0] = temps1[0]
                            speed1[1] = temps1[1]
                            speed2[0] = temps2[0]
                            speed2[1] = temps2[1]
                            temps1[0] = 0
                            temps1[1] = 0
                            temps2[0] = 0
                            temps2[0] = 0
                            pflag = False
                    elif x>90 and x < 150:
                        if speed1[0]>0:
                            speed1[0] = speed1[0]+1
                        else:
                            speed1[0] = speed1[0]-1
                        if speed1[1]>0:
                            speed1[1] = speed1[1]+1
                        else:
                            speed1[1] = speed1[1]-1
                        if speed2[0]>0:
                            speed2[0] = speed2[0]+1
                        else:
                            speed2[0] = speed2[0]-1
                        if speed2[1]>0:
                            speed2[1] = speed2[1]+1
                        else:
                            speed1[1] = speed2[1]-1
                    elif x>170 and x<230:
                        if speed1[0]>0:
                            speed1[0] = speed1[0]-1
                        else:
                            speed1[0] = speed1[0]+1
                        if speed1[1]>0:
                            speed1[1] = speed1[1]-1
                        else:
                            speed1[1] = speed1[1]+1
                        if speed2[0]>0:
                            speed2[0] = speed2[0]-1
                        else:
                            speed2[0] = speed2[0]+1
                        if speed2[1]>0:
                            speed2[1] = speed2[1]-1
                        else:
                            speed1[1] = speed2[1]+1
                    elif x>250 and x<310:
                        flag = False
         
    screen.fill(black)
    my_out = ("touch at "+str(x)+","+str(y))
    cord_surface = font_cord.render(my_out, True, WHITE)
    rect = cord_surface.get_rect(center = (160,120))
    screen.blit(cord_surface,rect)
    if flag == False:              
        for my_text, text_pos in buttons.items():
            text_surface = font_quit.render(my_text, True, WHITE)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)

    elif flag == True:
        for my_text, text_pos in buttons2.items():
            text_surface = font_buttons.render(my_text, True, WHITE)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect)
        
            # Erase the Work space
    screen.blit(ball1, ballrect1) 
    screen.blit(ball2, ballrect2)
    pygame.display.flip()
    
    if not gpio.input (27):
		pygame.quit()
		sys.exit(0) 
    
