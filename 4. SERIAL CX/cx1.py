from machine import UART                    # library
import time                         
uart = UART(0, baudrate=115200)             # UART configuration
while True:
  data=uart.read()                          # receive data
  print(data)                               # send data
  
  
