from random import uniform
from tkinter import *

newsens = f'  "MouseSensitivity" : {round(uniform(0.1,0.6),2)}, \n'

#def TarkovSens(CFGPath):
    #print(round(uniform(0.1, 0.5),2))
with open("Control.ini", "r") as file:
    filedata = file.read()

with open("Control.ini", "r") as file:        
    for line in file:
        if "MouseSensitivity" in line:
            oldsens = line


print(oldsens)
filedata = filedata.replace(oldsens, newsens)

with open("Control.ini" , "w") as file:
    file.write(filedata)










