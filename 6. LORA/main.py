#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file, or
# available at https://www.pycom.io/opensource/licensing
#

import time
from machine import I2C, Pin
from scd30 import SCD30


i2c = I2C(2)
scd30 = SCD30(i2c, 0x61)

while True:
    # Wait for sensor data to be ready to read (by default every 2 seconds)
    while scd30.get_status_ready() != 1:
        time.sleep_ms(200)
    (co2,temp,hum)=scd30.read_measurement()
        #-3
    temp -=3
    print("co2",co2)
    print("temp",temp)
    print("hum",hum)



     