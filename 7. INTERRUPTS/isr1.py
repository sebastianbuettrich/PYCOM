from machine import Pin
import time
i=1
def pin_handler(arg):
    print("got an interrupt in pin %s" % (arg.id()))
    global i
    i+=1
    print(i)
    
led1 = Pin('P9', mode=Pin.OUT)
p_in = Pin('P10', mode=Pin.IN,pull=Pin.PULL_UP)
p_in.callback(Pin.IRQ_FALLING, pin_handler)

while True:
    print("main code")
    led1.value(1)
    time.sleep(i)
    led1.value(0)
    time.sleep(i)
