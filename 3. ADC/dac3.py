from machine import ADC,DAC 
import time
dac = DAC('P22')                       # create a DAC object
adc = ADC()                            # object
channel1 = adc.channel(pin='P13')      # define the pin

while True:
    value = channel1.value()           # reading the channel 1
    output=value/4095                  # output 0:1
    dac.write(output)                  # pwm write
    mes=output*10                      # output 1: 10
    print("PWM:" + str(mes))           # sending messages
    time.sleep(1)                      # machine waits for 1 seg
