from machine import Pin
import time
led = Pin('P9', mode = Pin.OUT) # pin 9 as output
button = Pin('P8', mode = Pin.IN) # pin 8 as input

while True:
    if(button() == 0):  # state change condition
        led.value(1)  #true, led on
    else:
        led.value(0) # false, led off
