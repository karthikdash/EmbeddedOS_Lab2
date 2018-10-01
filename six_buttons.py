#Week 2 Lab 1
#Date: September 10, 2018
#created by Chirag Wadhwani (cw844) and Karthikeshwar Dasaraju (kd453)
#This code check if the correct button has been pressed on the piTFT and displays the button pressed. It also exposes us to the RPi GPIO I/O pin. It checks the functionality of 4 pins.
# We chose GPIO6 and GPIO19 as inputs for external buttons


import RPi.GPIO as gpio
import time
import os
import sys

# Set pin mode to Broadcom
gpio.setmode(gpio.BCM)
startPin = gpio.setup(17, gpio.IN, pull_up_down=gpio.PUD_UP)
stopPin = gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_UP)
fwdtPin = gpio.setup(23, gpio.IN, pull_up_down=gpio.PUD_UP)
rwdPin = gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_UP)

fwd30Pin = gpio.setup(5, gpio.IN)
rwd29Pin = gpio.setup(19, gpio.IN)

# Infinite loop
while True:
    # Delay to improve response of button press.
    time.sleep(0.2)
    if not gpio.input(17):
        print 'Button 17 has been pressed.'

    if not gpio.input(22):
        print 'Button 22 has been pressed.'

    if not gpio.input(23):
        print 'Button 23 has been pressed.'
    # GPIO6 will read external button
    if gpio.input(5):
        print 'Button 5 has been pressed.'

    # GPIO19 will read external button
    if gpio.input(19):
        print 'Button 19 has been pressed.'

    if not gpio.input(27):
        print 'Button 27 has been pressed.'
        print 'Exiting the program.'
        # Exit the python program
        sys.exit(0)
