from machine import Pin
import time
led = Pin('P9', mode = Pin.OUT)
button = Pin('P8', mode = Pin.IN)
on=False
while True:
    if(button() == 0):
        time.sleep_ms(200)
        on=on^1
        if on == True:
            print("led on")
            led.value(1)
        else:
            print("led off")
            led.value(0)
