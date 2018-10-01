# lab2 Week 1
# Created by Chirag Wadhwani (cw844) and Karthik D. (kd453)
# Code to control mplayer from fifo
# Interrupts for button read
import RPi.GPIO as gpio
import time
import os
import subprocess
import sys

gpio.setmode(gpio.BCM)
startPin = gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
stopPin = gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_UP)
fwdtPin = gpio.setup(23, gpio.IN, pull_up_down=gpio.PUD_UP)
rwdPin = gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)

# External buttons
fwd30Pin = gpio.setup(5, gpio.IN)
rwd29Pin = gpio.setup(19, gpio.IN)


def GPIO5_callback(channel):
    os.system('echo seek 30 > videoplayer')

def GPIO19_callback(channel):
    os.system('echo seek -30 > videoplayer')

def GPIO17_callback(channel):
    os.system('echo p > videoplayer')

def GPIO22_callback(channel):
    os.system('echo seek 10 > videoplayer')

def GPIO23_callback(channel):
    os.system('echo seek -10 > videoplayer')

def GPIO27_callback(channel):
    os.system('echo quit > videoplayer')
    gpio.cleanup()
    sys.exit(0)

gpio.add_event_detect(5, gpio.FALLING, callback=GPIO5_callback, bouncetime=300)
gpio.add_event_detect(19, gpio.FALLING, callback=GPIO19_callback, bouncetime=300)
gpio.add_event_detect(17, gpio.FALLING, callback=GPIO17_callback, bouncetime=300)
gpio.add_event_detect(22, gpio.FALLING, callback=GPIO22_callback, bouncetime=300)
gpio.add_event_detect(23, gpio.FALLING, callback=GPIO23_callback, bouncetime=300)
gpio.add_event_detect(27, gpio.FALLING, callback=GPIO27_callback, bouncetime=300)
start_time = time.time()
try:
    while True:
        # time.sleep(0.000002)
        if time.time() - start_time > 10:
            break
except KeyboardInterrupt:
    gpio.cleanup() # clean up GPIO on CTRL+C exit
gpio.cleanup()
