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

def set_number(number):
    global operanting, result

    if len(operanting) == 2:
        operanting[0] = operanting[1]
        operanting.pop()
        operanting.append(number)
        print("\n", operanting)
        result = True
    else:
        operanting.append(number)
        print("\n", operanting)

        result = True

def symbol(symbol, display, expr):
    global operator, oper
    num = eval(display.cget("text"))
    set_number(num)
    operator=symbol
    print("\n", operator)
    expression(symbol, expr)

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
    elif operator == 'x':
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

def porcent(display):

    global result
    previousvalue = eval(display.cget("text"))
    newvalue = round(0.01 * previousvalue, 14)
    display.config(text = str(newvalue))
    result=True

def expression(symbol, display):
    global operator
    t = len(operanting)
    n1 = operanting[0]
    if t == 1:
        phrase = (' {} {} '.format(n1, symbol))
    else:   
        n2 = operanting[1]
        phrase = ('{} {} {} = '.format(n1, operator, n2))
    display.config(text = phrase)
    
def igual(display, expr):
    num = eval(display.cget("text"))
    set_number(num)
    make_operation(display)
    expression("=", expr)
