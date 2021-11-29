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

from machine import UART                    # library
import time                         
uart = UART(0, baudrate=115200)             # UART configuration
while True:
  data=uart.read()                          # receive data
  print(data)                               # send data
  
  
