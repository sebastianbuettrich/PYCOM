from machine import Pin
import time
# individual configuration
led1 = Pin('P13', mode=Pin.OUT) #p13 as output
led2 = Pin('P14', mode=Pin.OUT) #p14 as output
led3= Pin('P15', mode=Pin.OUT)  #p15 as output
led4 = Pin('P16', mode=Pin.OUT)  #p16 as output

while True:
    led1.value(1)     #turn on led 1 and 2
    led2.value(1)
    time.sleep(1)     # wait 1 sec
    led3.value(1)     #turn on led 3 and 4
    led4.value(1)
    time.sleep(2)     # wait 2 sec
    led3.value(0)     #turn off led 3 and 4
    led4.value(0)
    time.sleep(2)     # wait 2 sec
    led1.value(1)     #turn off led 1 and 2
    led2.value(1)
    time.sleep(2)     # wait 2 sec
