from machine import DAC 
import time

dac = DAC('P22')        # create a DAC object
while True:
    print("OUTPUT 50%")
    dac.write(0.5)                  # set output to 50%
    time.sleep(10)
    print("OUTPUT 80%")
    dac.write(0.8)                  # set output to 80%
    time.sleep(10)    
