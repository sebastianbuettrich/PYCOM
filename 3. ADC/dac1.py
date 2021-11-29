#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: dac1.py -> Simple digital analog test
# IoT course
#

from machine import DAC 
import time

dac = DAC('P22')        # create a DAC object
while True:
    print("OUTPUT 50%")
    dac.write(0.5)                  # set output to 50%
    time.sleep(10)
    print("OUTPUT 80%")
    dac.write(0.8)                  # set output to 80%
    time.sleep(10)    
