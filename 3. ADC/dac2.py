from machine import DAC, PWM
import time
pwm = PWM(0, frequency=500)  # use PWM timer 0, with a frequency of 500Hz
dac = DAC('P22')        # create a DAC object
pwm_c = pwm.channel(0, pin='P23') # create pwm channel on pin P23 with a duty cycle of 50%
while True:
    for i in range(10):
        dato=i/10
        pwm_c.duty_cycle(dato) # change the duty cycle to 30%
        print(dato)
        time.sleep(1)
    pwm_c.duty_cycle(0.0)    
    print("OUTPUT 50%")
    dac.write(0.5)                  # set output to 50%
    time.sleep(10)
    print("OUTPUT 80%")
    dac.write(0.8)                  # set output to 80%
    time.sleep(10)    
