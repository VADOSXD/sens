from random import uniform
from tkinter import *



def TarkovSens(CFGPath):
    SensDigit = round(uniform(0.1, 0.6), 2)
    newsens = f'  "MouseSensitivity" : {SensDigit}, \n'
    aimsens = f'  "MouseAimingSensitivity" : {SensDigit}, \n'
    with open(f"{CFGPath}", "r") as file:
        filedata = file.read()

    with open(f"{CFGPath}", "r") as file:        
        for line in file:
            if "MouseAimingSensitivity" in line:
                oldaimsens = line 
            if "MouseSensitivity" in line:
                oldsens = line


    print(oldsens)
    filedata = filedata.replace(oldsens, newsens)
    filedata = filedata.replace(oldaimsens, aimsens)

    with open(f"{CFGPath}" , "w") as file:
        file.write(filedata)

TarkovSens("/Users/kuzmenkovvadim/Documents/sensrandomizer/Control.ini")








