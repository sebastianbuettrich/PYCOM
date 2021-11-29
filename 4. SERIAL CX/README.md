# SERIAL COMMUNICATION
## Theory:
### Functionality:



### Libraries:
```
from machine import UART #library 
```
### Code Structures:
```
uart = UART(0, baudrate=115200)        # UART configuration
data=uart.read()        # receive data    print(data)                            # send data
```
## Examples:
```
cx1.py -> Read/Write chart/strings
cx2.py -> convert string to int serial cx
project -> converting vowels in '*'
```
