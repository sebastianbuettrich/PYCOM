from machine import UART
import time
uart = UART(0, baudrate=115200)
lst = []
while True:
    if uart.any() > 0:   
        print("yes")       # returns the number of characters waiting
        data=uart.read()   # read all available characters
        lst=list(data)     # convert data in list
        for a in range(len(lst)):  # for cicle in range 0 to tam list
            lst[a]=int(lst[a])     # convert to int
            lst[a]=lst[a]-48       #convert a number
            print(lst[a])          # print the number
