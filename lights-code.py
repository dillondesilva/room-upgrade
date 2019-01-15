'''
Code for neopixels which will light up
when a radio signal is received
'''

from microbit import *
import radio
import neopixel

from random import *

radio.on()
radio.config(channel=63)

neopixels = neopixel.NeoPixel(pin13, 12)

def display_new_visuals():
    for n in range(len(neopixels)):
        rand_red = randint(1, 255)
        rand_green = randint(1, 255)
        rand_blue = randint(1, 255)
        
        neopixels[n] = (rand_red, rand_green, rand_blue)
        
    neopixels.show()
    
while True:
    msg = radio.receive()
    if msg:
        if msg == 'display:on' or msg == 'alternate':
            display_new_visuals()
            
        if msg == 'display:off':
            neopixels.clear()