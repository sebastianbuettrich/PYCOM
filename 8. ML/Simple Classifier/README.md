# Simple Binary Classifier #

## Introduction ##

Machine learning algorithms can describe phenomena or human behavior through complex mathematical functions. Therefore, they need high computational resources. However, tinyML is designed to run on small devices to improve the making decision process inside of it. Consequently, the classification algorithms learn from past experiences 
(training set) to assign new instances a pre-defined group (label). 

## Step 1: Data acquisition ##

### System descryption: ###

The electronic system proposed is to detect if the SCD30 (CO2, temperature, and humidity) sensor has been tampered with by people blowing on him. Therefore, the electronic system can detect two labels: adequate environmental data and tampered data. The code is developed in Python. 

### Assembling the training and test set###
 The electronic system takes samples every 5 seconds for three variables sending them by Serial communication to a server/desktop to store them. As a result, the dataset has 400 samples for label 1 and 200 samples for label 2. The dataset can be download here: [link](https://github.com/puldavid87/PYCOM/blob/main/8.%20ML/Simple%20Classifier/data.csv).
 
 To receive the data from the computer. The Python code is:
 ```
 import pandas as pd
import serial 

dataset=pd.DataFrame(columns=["co2","temp","hum"])
com=serial.Serial(port='COM12', baudrate=115200)
i=0
while True:
    if(com.in_waiting > 0):
        datos=com.readline()
        val=datos.split()
        if len(val)>4:
            if i<200:
                dataset=dataset.append({'co2' : val[0].decode("utf-8") , 
                                        'temp' : val[2].decode("utf-8") ,
                                        'hum' : val[4].decode("utf-8") },
                                        ignore_index=True)
                i+=1
                print(i)
            else:
                com.close()

dataset.to_csv("data1.csv")
 ```
## Step 2: Model construction ##
## Step 3: Export the inference ## 
## Step 4: Real tests ## 
