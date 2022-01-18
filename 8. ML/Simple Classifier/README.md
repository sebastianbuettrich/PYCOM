# Simple Binary Classifier #

## Introduction ##

Machine learning algorithms can describe phenomena or human behavior through complex mathematical functions. Therefore, they need high computational resources. However, tinyML is designed to run on small devices to improve the making decision process inside of it. Consequently, the classification algorithms learn from past experiences 
(training set) to assign new instances a pre-defined group (label). 

## Step 1: Data acquisition ##

### System descryption: ###

The electronic system proposed is to detect if the SCD30 (CO2, temperature, and humidity) sensor has been tampered with by people blowing on him. Therefore, the electronic system can detect two labels: adequate environmental data and tampered data. The code is developed in Python. 

### Assembling the training and test set ###
 The electronic system takes samples every 5 seconds for three variables sending them by Serial communication to a server/desktop to store them. As a result, the dataset has 400 samples for label 1 and 200 samples for label 2. The dataset can be download here: [link](https://github.com/puldavid87/PYCOM/blob/main/8.%20ML/Simple%20Classifier/data.csv).
 
 To receive the data and store them from the computer, the Python code is:
 ```
#Libraries:

import pandas as pd
import serial 
#create the dataframe
dataset=pd.DataFrame(columns=["co2","temp","hum"])
# serial communication object
com=serial.Serial(port='COM12', baudrate=115200)
#confirmation variable
i=0
while True:
#waits to incoming data
    if(com.in_waiting > 0):
     # variabe recives data
        datos=com.readline()
        # variable divides the data by separator ";"
        val=datos.split()
        # confirmation the data separation
        if len(val)>4:
        #400 samples, you can change the number for samples.
            if i<400:
                # store data in the dataframe
                dataset=dataset.append({'co2' : val[0].decode("utf-8") , 
                                        'temp' : val[2].decode("utf-8") ,
                                        'hum' : val[4].decode("utf-8") },
                                        ignore_index=True)
                #confirmation
                i+=1
                print(i)
            else:
               # close the COM port.
                com.close()
#export to csv the model
dataset.to_csv("data1.csv")
 ```
The code in the electronic device is:

```
import time
import math
import pycom
from machine import UART                    
from machine import I2C
from scd30 import *
uart = UART(0, baudrate=115200)             # UART configuration
pycom.heartbeat(False)  # disable the heartbeat LED
i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
# NOTE: Could not make it work using the ESP32 hardware I2C buses (0 & 1), 
# but the bitbanged software bus (2) works
# Yay for libraries!
sensor = SCD30(i2c, 0x61)
while True:
    for i in range (500):
         # Wait for sensor data to be ready to read (by default every 2 seconds)
        if sensor.get_status_ready() != 1:
            time.sleep_ms(200)
        (co2, temperature, hum) = sensor.read_measurement()
            # Adjust for PCB heating effect. 
        temperature -= 3 # NOTE: Found this value somewhere online
        #send the information
        print(round(co2,2),';',round(temperature,2),';',round(hum,2))
        time.sleep_ms(5000)
```

## Step 2: Model construction ##

### Split the data set in training and test set ###
```
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

dataset=pd.read_csv('data.csv', sep=';')
X= dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values
X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=0.2, random_state=0)

#Figure because we can :)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_train[:,0],X_train[:,1],X_train[:,2],c=y_train+1)
ax.set_xlabel("CO2")
ax.set_ylabel("Temperature")
ax.set_zlabel("HUmidity")
plt.show()
```
![Figure](https://github.com/puldavid87/PYCOM/blob/main/8.%20ML/Simple%20Classifier/fig.png)

### Classification models ### 

To see and understand better, you can check this: [Support vector machines](https://scikit-learn.org/stable/modules/svm.html) and [Decision tree](https://scikit-learn.org/stable/modules/tree.html).

### SVM model ###
```
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix

#train the model
classifiert=SVC(kernel='linear', gamma=0.001).fit(X_train,y_train)
y_pred=classifier.predict(X_test)
# classification performance
print(confusion_matrix(y_test,y_pred))
```
### Decision tree model ###
```
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix


#train the model
tree_model = DecisionTreeClassifier().fit(X_train,y_train) 
y_pred =tree_model.predict(X_test)
# classification performance
print(confusion_matrix(y_test,y_pred)
```
## Step 3: Export the inference ## 
Library for export the model: [m2cgen](https://github.com/BayesWitnesses/m2cgen)
### SVM model ###
```
import m2cgen as m2c
code1=m2c.export_to_python(classifier)
print(code1)

```
### Decision tree model ###
```
import m2cgen as m2c
code2=m2c.export_to_python(tree_model)
print(code2)

```

## Step 4: Real tests ## 

The model can be exported in an external file .py to call it in the main function to run it in the electronic device.

```
import time
import math
import pycom
from machine import UART                    
from machine import I2C
from scd30 import *
from svm_model import svm
from tree_model import tree
uart = UART(0, baudrate=115200)             # UART configuration
pycom.heartbeat(False)  # disable the heartbeat LED
i2c = I2C(2) # create and use default PIN assignments (P9=SDA, P10=SCL)
# NOTE: Could not make it work using the ESP32 hardware I2C buses (0 & 1), 
# but the bitbanged software bus (2) works
# Yay for libraries!
sensor = SCD30(i2c, 0x61)


while True:
    for i in range (500):
         # Wait for sensor data to be ready to read (by default every 2 seconds)
        if sensor.get_status_ready() != 1:
            time.sleep_ms(200)
        (co2, temperature, hum) = sensor.read_measurement()
            # Adjust for PCB heating effect. 
        temperature -= 3 # NOTE: Found this value somewhere online
        data=[co2,temperature,hum] # put in array the sensor data
        #make the prediction
        y_pred=svm(data)
        #send the information and the label
        print(round(co2,2),';',round(temperature,2),';',round(hum,2), ';' y_pred)
        time.sleep_ms(2000)
        
```
