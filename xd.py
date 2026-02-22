from random import uniform
from tkinter import *



def TarkovSens(CFGPath):
    newsens = f'  "MouseSensitivity" : {round(uniform(0.1,0.6),2)}, \n'
    with open(f"{CFGPath}", "r") as file:
        filedata = file.read()

    with open(f"{CFGPath}", "r") as file:        
        for line in file:
            if "MouseSensitivity" in line:
                oldsens = line


    print(oldsens)
    filedata = filedata.replace(oldsens, newsens)

    with open(f"{CFGPath}" , "w") as file:
        file.write(filedata)

TarkovSens("/Users/kuzmenkovvadim/Documents/sensrandomizer/Control.ini")








