# ANALOG-DIGITAL * DIGITAL-ANALOG CONVERTER
## Theory:
### Functionality:

ADC:

To describe a phenomenon, it is necessary to represent it the most of the cases in voltage. Then, this signal can be scaled to finite numbers called registers. Generally, these registers can be 10,12, and 16 bits.  

DAC: 
Most used in pulse-width modulation. The duty cycle of a periodic signal is the relative width of its positive part about the period


PinOut:
![Esta es una imagen](https://github.com/puldavid87/PYCOM/blob/main/fipy-pinout.png)

### Libraries:
```
from machine import ADC
import time
```
### Code Structures:
```
adc = machine.ADC()             # create an ADC object
apin = adc.channel(pin='P16')   # create an analog pin on P16
dac = machine.DAC('P22')        # create a DAC object
dac.write(0.5)                  # set output to 50%
from machine import PWM
pwm = PWM(0, frequency=5000)  # use PWM timer 0, with a frequency of 5KHz
```
## Examples:
```
io1.py -> Simple Output ports configuration (Hello World..!!)
io2.py -> For and If cycles with output ports configuration
io3.py -> Simple Input configuration
io4.py -> button configuration avoiding rebounds
```
