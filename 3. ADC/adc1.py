#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: adc1.py -> Simple analog digital test
# IoT course
#

from machine import ADC
import time

adc = ADC()                            # object
channel1 = adc.channel(pin='P13')      # define the pin

while True:
    value = channel1.value()           # reading the channel 1
    datos=channel1()                   # another way
    voltage=(datos*(3.3))/4095         # convert the integer to voltage 
    print("ADC value:" + str(value))   # sending messages
    print("ADC value:" + str(datos))
    print("Voltage:" + str(voltage))
    time.sleep(5)                      # machine waits for 5 seg
