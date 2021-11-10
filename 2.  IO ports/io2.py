
from machine import Pin
import time
# individual configuration
led1 = Pin('P12', mode=Pin.OUT) #pin 12 out
led1 = Pin('P12', mode=Pin.OUT) #pin 12 out
led2 = Pin('P11', mode=Pin.OUT) #pin 11 out
led3= Pin('P10', mode=Pin.OUT)  #pin 10 out
led4 = Pin('P9', mode=Pin.OUT)  #pin 9 out
toggle=0
x=0
while True:
# 5 times led1 blinks (toggle-> 1 to 0)  in 1 sec  
    for i in range(10):
        print("led1 blinks",i)
        led1.toggle()
        time.sleep(1)
# 5 times led2 blinks with break in 10 ms
    for j in range(10):
        print("led2 blinks:",j)
        led2.value(1)
        time.sleep_ms(10)
        led2.value(0)
        time.sleep_ms(10) 
        if j == 5:
            break
# 5 times led3 blinks with toggle fuction in 500 us
    for k in range(5):
        print("led3 blinks:",k)
        led3.value(toggle)
        toggle=toggle^1;
        time.sleep_us(500)
        led3.value(toggle)
        time.sleep_ms(500)
# 5 times led 4 blinks before all for cicles in 1 sec
    if x<6:
        print("led4 blinks:",x)
        led4.toggle()
        time.sleep(1)
        ++x;
