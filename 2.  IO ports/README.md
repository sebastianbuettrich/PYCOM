# Input / Output ports
## Theory:
# Functionality:
```
Output:
The simple way to understand embedded systems (pycom) is when the system only has two states, true (3.3 volts) and false (0 volts). We can test these states when the system sends or receives them. We can send these states to another electronic part such as leds. To do this, we must select the pin or pins that we will use. Therefore, the figure shows the pin distribution, each pin called GPIO can be used to send or receive logic states. Also, we need to stop the machine for several seconds to see what happens with leds. If we do not stop to machine, the system will run so fast that we can not see if the LEDs are on or off.   

Input: 
```

# Code Structures:
```
Pin('PIN', mode=Pin.MODE)
PIN-> selected pin (P8,P9)
MODE-> OUT
       IN
```
### Examples:
```
io1.py -> Simple Output ports configuration (Hello World..!!)
io2.py -> For and If cycles with output ports configuration
```
