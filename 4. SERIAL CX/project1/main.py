from machine import UART
import time
uart = UART(0, baudrate=115200)
lst = []
while True:
    if uart.any() > 0:   
        data=uart.read()   # read all available characters
        lst=list(data)     # convert data in list
        for i in range (len(data)):
            lst[i]= chr(lst[i])
            lst[i]=lst[i].upper()
            if lst[i] == 'A' or lst[i] == 'E' or lst[i] == 'I' or lst[i] == 'O' or lst[i] == 'U':
                lst[i]='*' 
        print(lst)


    
