#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: dac4.py -> Input port and PWM configuration
# IoT course
#


from machine import DAC, Pin 
import time
dac = DAC('P22')                       # create a DAC object
button=Pin('P13', mode=Pin.IN)
cont=1                                 # variable
while True:
    if(button())==0:                   # activate buton
        time.sleep_ms(200)             # anti-bounce
        if cont <=10:                  # set the pwm 1-10 
            cont+=1                    # pwm+++
            output=cont/10             # convert pwm between 0,1->1
            dac.write(output)                  # pwm write
            print("PWM:" + str(cont))           # sending messages
        else:
            cont=0
