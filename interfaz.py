# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 15:05:54 2021

@author: paur
"""

import serial, time
import tkinter as tk
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk) 
from matplotlib import pyplot as plt
on=False
signal=[]
x=[]
x_filter=[]
def Conection ():
    global on
    on=on^1
    if on==True:
        print("on")
        button_com.config(bg="green")
        INPUT = input_com.get("1.0", "end-1c")
        input_com.delete("1.0",tk.END)
        input_com.insert(tk.END,"CONECTED")
        #cx=serial.Serial(port=INPUT, baudrate=115200, timeout=1, write_timeout=1)
    else:
        print("off")
        button_com.config(bg="red") 
        input_com.delete("1.0",tk.END)
        input_com.insert(tk.END,"PORT CLOSED")
        
        
def dataac ():
    samples = str(input_data.get("1.0", "end-1c"))
    number=int(samples)
    global signal
    global x_filter
    signal.clear()
    x.clear()
    x_filter.clear()
    #put zeros
    for i in range (number):
        signal.append(0)
        x.append(i)
        x_filter.append(0)
        
    for i in range (number):
        signal[i]=i*random.randrange(1,5)
        x_filter[i]=i*random.randrange(2,4)

def filters  (x,y):
    ax.clear()
    ax.plot(x,y, label="original", color="red")
    ax.plot(x_filter,y, label="filter", color="blue")
    canvas.draw()
    print("no")

     
root = tk.Tk()
############################################################################
###########################  ROOT INTERFACE  ############################### 
############################################################################

root.geometry('1400x750')
root.resizable(False, False)
root.title('FILTER ANALYSIS')

############################################################################
###########################   FRAME CREATION ###############################
############################################################################

top_frame = tk.Frame(root, width=500, height=200, pady=3)
center = tk.Frame(root, width=1400, height=600, padx=3, pady=3)

############################################################################
###########################   SUBFRAME CREATION  ###########################
############################################################################

center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = tk.Frame(center, width=1400, height=400)
#ctr_right = tk.Frame(center, width=1400, height=300)

ctr_left.grid(row=0, column=0, sticky="ns")
#ctr_right.grid(row=1, column=0, sticky="nsew")

############################################################################
################## layout all of the main containers  ######################
############################################################################
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")

############################################################################
####################### TOP FRAME CONFIGURATION  ###########################
############################################################################

############DATA ACQUISITION###############################################
###### SERIAL COMMUNICATION WITH THE EMBEDDED SYSTEM
###########################################################################
label_com=tk.Label(top_frame,text="Insert COM Port:")
input_com=tk.Text(top_frame, height = 2,
                width = 15,bg = "light yellow")
button_com = tk.Button(top_frame, text="COM CONECTION", 
                   fg="black",
                   command=Conection)

##################### NUMBER OF SAMPLES  ##################################
label_data=tk.Label(top_frame,text="Insert number of samples:")

input_data=tk.Text(top_frame, height = 2,
                width = 15,
                bg = "light yellow")

button_data = tk.Button(top_frame, 
                   text="START", 
                   fg="black",
                   command=dataac)

##################   GRAPHICAL    ########################################## 
#graphs
figure = plt.Figure(figsize=(5,5))
canvas = FigureCanvasTkAgg(figure, ctr_left)
canvas.get_tk_widget().place(x=0,y=0,width=1000,height=300)
ax = figure.add_subplot(111)


###########################  FILTER DESIGN ###############################
########################## WINDOWS FILER SIZE ############################

label_grap=tk.Label(top_frame,text="Insert windows size:")

input_grap=tk.Text(top_frame, height = 2,
                width = 15,
                bg = "light yellow")


button_grap = tk.Button(top_frame, 
                   text="STARTER", 
                   fg="black",
                    command= lambda:filters(x,signal))

############################  IIR FILTER CONTROLLER #######################
###########################################################################


label_IIR=tk.Label(top_frame,text="IIR PAREMETERS")
label_f1=tk.Label(top_frame,text="LOW FREQUENCY")
label_f2=tk.Label(top_frame,text="HIGH FREQUENCY")
label_order=tk.Label(top_frame,text="ORDER")
input_low=tk.Text(top_frame, height = 2,
                width = 10,
                bg = "light yellow")
input_high=tk.Text(top_frame, height = 2,
                width = 10,
                bg = "light yellow")

Lb1 = tk.Listbox(top_frame,height = 5,
                width = 5)
Lb1.insert(1, "1")
Lb1.insert(2, "3")
Lb1.insert(3, "5")
Lb1.insert(4, "7")


label_com.grid(row = 0, column = 0, pady = 2)
input_com.grid(row = 0, column = 1, pady = 2)
button_com.grid(row = 0, column = 2, pady = 2)
label_data.grid(row = 0, column = 3, pady = 2)
input_data.grid(row = 0, column = 4, pady = 2)
button_data.grid(row = 0, column = 5, pady = 2)
label_grap.grid(row = 0, column = 6, pady = 2)
input_grap.grid(row = 0, column = 7, pady = 2)
button_grap.grid(row = 0, column =8, pady = 2)
###############################################
label_IIR.grid(row = 1, column = 0, pady = 2)
label_f1.grid(row = 2, column = 0, pady = 2)
label_f2.grid(row = 3, column = 0, pady = 2)
input_low.grid(row = 2, column = 1, pady = 2)
input_high.grid(row = 3, column = 1, pady = 2)
label_order.grid(row = 1, column = 2, pady = 2)
Lb1.grid(row = 2, column = 2, pady = 2 )

root.mainloop()
