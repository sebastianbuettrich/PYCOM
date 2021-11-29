
#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: dac3.py -> ADC and DAC configuration
# IoT course
#


from machine import ADC,DAC 
import time
dac = DAC('P22')                       # create a DAC object
adc = ADC()                            # object
channel1 = adc.channel(pin='P13')      # define the pin

while True:
    value = channel1.value()           # reading the channel 1
    output=value/4095                  # output 0:1
    dac.write(output)                  # pwm write
    mes=output*10                      # output 1: 10
    print("PWM:" + str(mes))           # sending messages
    time.sleep(1)                      # machine waits for 1 seg
