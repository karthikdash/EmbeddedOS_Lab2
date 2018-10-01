# lab 2 - Week 1
# Created by Chirag Wadhwani(cw844) and Karthik D.(kd453)
# Code to control mplayer from fifo
import RPi.GPIO as gpio
import time
import os
import sys
from threading import Timer
gpio.setmode(gpio.BCM)
startPin = gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
stopPin = gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_UP)
fwdtPin = gpio.setup(23, gpio.IN, pull_up_down=gpio.PUD_UP)
rwdPin = gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)

# External buttons
fwd30Pin = gpio.setup(5, gpio.IN)
rwd29Pin = gpio.setup(19, gpio.IN)


start_time = time.time()

while True:
    # time.sleep(0.000002)
    if time.time() - start_time > 10:
        break
    if not gpio.input(17):
        os.system('echo p > videoplayer')

    if not gpio.input(22):
        os.system('echo seek 10 > videoplayer')

    if not gpio.input(23):
        os.system('echo seek -10 > videoplayer')

    if gpio.input(5):
        os.system('echo seek 30 > videoplayer')

    if not gpio.input(19):
        os.system('echo seek -30 > videoplayer')

    if not gpio.input(27):
        print '27'
        os.system('echo quit > videoplayer')
        sys.exit(0)
