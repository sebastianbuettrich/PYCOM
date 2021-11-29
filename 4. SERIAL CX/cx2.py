#!/usr/bin/env python
#
# Copyright (c) 2019, IT university of Copenhagen
#
# This software is licensed under the GNU GPL version 3 or any
# later version, with permitted additional terms. For more information
# see the Pycom Licence v1.0 document supplied with this file
# Code: cx2.py -> convert string to int serial cx
# IoT course
#

from machine import UART
import time
uart = UART(0, baudrate=115200)
lst = []
while True:
    if uart.any() > 0:   
        data=uart.read()   # read all available characters
        lst=list(data)     # convert data in list
        for a in range(len(lst)):  # for cicle in range 0 to tam list
            lst[a]=int(lst[a])     # convert to int
            lst[a]=lst[a]-48       #convert a number
            print(lst[a])          # print the number
