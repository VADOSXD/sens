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


    filedata = filedata.replace(oldsens, newsens)
    filedata = filedata.replace(oldaimsens, aimsens)

    with open(f"{CFGPath}" , "w") as file:
        file.write(filedata)

def ApexSens(CFGPath):
    ASens = f'mouse_sensitivity "{round(uniform(1.0, 2.5),2)}" \n'
    with open(f"{CFGPath}", "r") as file:
        filedata = file.read()

    with open(f"{CFGPath}", "r") as file:
        for line in file:
            if "mouse_sensitivity" in line:
                OldSens = line
    filedata = filedata.replace(OldSens, ASens)
    with open (f"{CFGPath}", "w") as file:
        file.write(filedata)

ApexSens("/Users/kuzmenkovvadim/Documents/sensrandomizer/settings.cfg")








