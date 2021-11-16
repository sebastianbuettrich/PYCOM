from machine import ADC
import time

adc = ADC()                            # object
channel1 = adc.channel(pin='P13')      # define the pin

while True:
    value = channel1.value()           # reading the channel 1
    datos=channel1()                   # another way
    voltage=(datos*(3.3))/4095         # convert the integer to voltage 
    print("ADC value:" + str(value))   # sending messages
    print("ADC value:" + str(datos))
    print("Voltage:" + str(voltage))
    time.sleep(5)                      # machine waits for 5 seg
