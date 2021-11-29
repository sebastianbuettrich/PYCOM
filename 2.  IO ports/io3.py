#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: io3.py -> Simple Input configuration
# IoT course
#

from machine import Pin
import time
led = Pin('P9', mode = Pin.OUT) # pin 9 as output
button = Pin('P8', mode = Pin.IN) # pin 8 as input

while True:
    if(button() == 0):  # state change condition
        led.value(1)  #true, led on
    else:
        led.value(0) # false, led off
