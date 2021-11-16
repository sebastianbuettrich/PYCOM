from machine import DAC, Pin 
import time
dac = DAC('P22')                       # create a DAC object
button=Pin('P13', mode=Pin.IN)
cont=1
while True:
    if(button())==0:
        time.sleep_ms(200)
        if cont <=10:
            print("click")
            cont+=1
            output=cont/10
            dac.write(output)                  # pwm write
            print("PWM:" + str(cont))           # sending messages
        else:
            cont=0
