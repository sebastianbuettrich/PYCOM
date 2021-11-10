from machine import Pin
import time
led = Pin('P9', mode = Pin.OUT)
button = Pin('P8', mode = Pin.IN)

while True:
    if(button() == 0):
        led.value(1)
    else:
        led.value(0)
