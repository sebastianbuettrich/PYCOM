#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: cx1.py -> Read/Write chart/strings
# IoT course
#
# Thanks Niels..!!
#


import time
import pycom
from machine import I2C
from scd30 import SCD30

pycom.heartbeat(False)  # disable the heartbeat LED

i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
# NOTE: Could not make it work using the ESP32 hardware I2C buses (0 & 1), 
# but the bitbanged software bus (2) works

# Yay for libraries!
scd30 = SCD30(i2c, 0x61)

while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    while scd30.get_status_ready() != 1:
        time.sleep_ms(200)
    (co2, temperature, relh) = scd30.read_measurement()
    
    # Adjust for PCB heating effect. 
    temperature -= 3 # NOTE: Found this value somewhere online
    
    print("============")
    print("CO_2: %.1f ppm" % co2)
    print("Temperature: %.1f C" % temperature)
    print("Rel. Humidity: %.1f%%" % (relh))
