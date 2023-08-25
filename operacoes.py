import tkinter as tk
import math as mt

def clear_text(display):
    newtext = display.cget("text")
    display.config(text=" ")

def set_text(txt, display):  
    previoustext = display.cget("text")
    newtext = previoustext + txt
    display.config(text=newtext)

def square(display):
    value = eval(display.cget("text"));
    newvalue = int(mt.pow(value, 2))
    display.config(text=str(newvalue))