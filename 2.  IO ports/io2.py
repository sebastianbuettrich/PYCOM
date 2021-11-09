from machine import Pin
import time
leds = ['p12','p11','p10','p9']
# First way
for i in leds:
    Pin(leds, mode=Pin.OUT)
#Second way
for i in range(len(leds)):
    Pin(leds[i], mode=Pin.OUT)
x=0
y=0
while True:
    for j in leds:
        print("Game 1")
        j.value(1)
        time.sleep(2)
        j.value(0)
    for i in range(len(leds)):
        print("Game 2")
        leds[i].value(1)
        time.sleep(2)
        leds[i].value(0)

    if  x < 4:
        print("Game 3")
        leds[x].value(1)
        time.sleep(2)
        leds[x].value(0)       
        time.sleep(2)
        ++x

    if y < 10:
        print("Game 4")
        for j in leds:
            j.value(1)
            time.sleep(2)
            j.value(0)
            time.sleep(2)
            ++y
