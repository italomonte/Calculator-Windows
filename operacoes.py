import tkinter as tk
import math as mt

result = False

def clear_text(display):
    global result
    display.config(text=" ")
    result = False

def delete(display):
    global result
    previoustext= display.cget("text")
    newtext = previoustext[:-1]
    display.config(text=newtext)
    result = False

def set_text(txt, display):  
    global result
    if result == True:
        clear_text(display)
        previoustext = display.cget("text")
        newtext = previoustext + txt
        display.config(text=newtext)
        result = False
    else:
        previoustext = display.cget("text")
        newtext = previoustext + txt
        display.config(text=newtext)
        result = False
    

def square(display):
    global result
    value = eval(display.cget("text"))
    newvalue = int(mt.pow(value, 2))
    display.config(text=str(newvalue))
    result = True

def inverse(display):
    global result
    previoustext = display.cget("text")
    newvalue = 1/eval(previoustext)
    display.config(text=str(newvalue))
    result = True