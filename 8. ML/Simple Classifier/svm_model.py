import pycom
from machine import I2C

def svm (input):
    var=(((-4.147148201257976) + (((((1480.18) * (input[0])) + ((22.19) * (input[1]))) + ((29.45) * (input[2]))) * (-0.004487416526825416))) + (((((33815.78) * (input[0])) + ((31.54) * (input[1]))) + ((61.83) * (input[2]))) * (0.00003564269526702233))) + (((((1221.28) * (input[0])) + ((27.05) * (input[1]))) + ((49.89) * (input[2]))) * (0.004451773831558377))
    if var < 0:
        return 1
    else:
        return 2