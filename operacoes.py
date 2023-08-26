import tkinter as tk
import math as mt

# global variable to know if old value is a result or just a random number
result = False

# global variabel to know what operation will be done
operator = " "

# global list to know which number will be used in operation
operanting = []

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

def set_number(display):
    global operanting, result
    number = eval(display.cget("text"))

    if len(operanting) == 2:
        operanting[0] = operanting[1]
        operanting.pop()
        operanting.append(number)
        result = True
    else:
        operanting.append(number)
        result = True

def symbol(symbol, display):
    global operator
    set_number(display)
    operator=symbol

def igual(display):
    set_number(display)
    make_operation(display)

def make_operation(display):
    global operator, result
    if operator == "+":
        newvalue = str(round(operanting[0] + operanting[1], 14))
        set_text(newvalue, display)
        result = True
    elif operator == '-':
        newvalue = str(round(operanting[0] - operanting[1], 14))
        set_text(newvalue, display)
        result = True
    elif operator == 'X':
        newvalue = str(round(operanting[0] * operanting[1], 14))
        set_text(newvalue, display)
        result = True
    elif operator == '/':
        newvalue = str(round(operanting[0] / operanting[1], 14))
        set_text(newvalue, display)
        result = True
def square(display):
    global result
    value = eval(display.cget("text"))
    newvalue = round((mt.pow(value, 2)), 14)
    display.config(text=str(newvalue))
    result = True

def inverse(display):

    global result
    previoustext = display.cget("text")
    newvalue = round(1/eval(previoustext), 14)
    display.config(text=str(newvalue))
    result = True

def squareroot(display):
    global result
    previoustext = display.cget("text")
    newvalue = round(mt.sqrt(eval(previoustext)), 14)
    display.config(text=str(newvalue))
    result=True