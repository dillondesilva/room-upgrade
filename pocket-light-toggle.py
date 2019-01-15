'''
Code for a microbit in my pocket to control lights. When button_a
is pressed, lights toggle on and off and button_b can switch designs
'''

from microbit import *
import radio

radio.on()
radio.config(channel=63)

ON_FLAG = False

while True:
    if button_a.was_pressed():
        if ON_FLAG:
            radio.send('display:off')
        else:
            radio.send('display:on')
            
        ON_FLAG = not ON_FLAG
        
    if button_b.was_pressed():
        radio.send('alternate')