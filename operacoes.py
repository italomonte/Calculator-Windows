import tkinter as tk
import math as mt

# global variable to know if old value is a result or just a random number
result = False
results = []

# global variabel to know what operation will be done
operator = " "

# global list to know which number will be used in operation
operanting = []

equal_clicked = False

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
    global operator, operanting, results, equal_clicked, result

    print("\n set_text antes")
    print("\n", "operanting: ", operanting, "results: ", results, "operator: ", operator, "equal_clicked: ", equal_clicked, "result: ", result,"\n")

    
    if result == True:
        clear_text(display)
        display.config(text=txt)
        result = False
    else:
        previoustext = display.cget("text")
        newtext = previoustext + txt
        display.config(text=newtext)
        result = False
    
    print("\n set_text depois")
    print("\n", "operanting: ", operanting, "results: ", results, "operator: ", operator, "equal_clicked: ", equal_clicked, "result: ", result,"\n")

def set_number(number):
    global operator, operanting, results, equal_clicked, result

    print("\n set_number antes")
    print("\n", "operanting: ", operanting, "results: ", results, "operator: ", operator, "equal_clicked: ", equal_clicked, "result: ", result,"\n")

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

    print("\n set_number depois")
    print("\n", "operanting: ", operanting, "results: ", results, "operator: ", operator, "equal_clicked: ", equal_clicked, "result: ", result,"\n")

def symbol(symbol, display, expr):
    global operator, operanting, results, equal_clicked, result

    print("\n symbol antes")
    print("\n", "operanting: ", operanting, "results: ", results, "operator: ", operator, "equal_clicked: ", equal_clicked, "result: ", result,"\n")

    num = eval(display.cget("text"))
    set_number(num)
    operator=symbol
    expression(symbol, expr)
    equal_clicked = False
    print("\n symbol depos")
    print("\n", "operanting: ", operanting, "results: ", results, "operator: ", operator, "equal_clicked: ", equal_clicked, "result: ", result,"\n")

def make_operation(display):
    global operator, operanting, results, equal_clicked, result

    print("\n makeoperation antes")
    print("\n", "operanting: ", operanting, "results: ", results, "operator: ", operator, "equal_clicked: ", equal_clicked, "result: ", result,"\n")
    if operator == "+":
        newvalue = str(round(operanting[0] + operanting[1], 14)) 
    elif operator == '-':
        newvalue = str(round(operanting[0] - operanting[1], 14))
    elif operator == 'x':
        newvalue = str(round(operanting[0] * operanting[1], 14))
    elif operator == '/':
        newvalue = str(round(operanting[0] / operanting[1], 14))
    
    result = True
    set_text(newvalue, display)
    results.append(eval(newvalue))
    equal_clicked = False

    print("\n makeoperation depois")
    print("\n", "operanting: ", operanting, "results: ", results, "operator: ", operator, "equal_clicked: ", equal_clicked, "result: ", result,"\n")

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
    global operator, operanting, results, equal_clicked, result

    print("\n igual antes")
    print("\n", "operanting: ", operanting, "results: ", results, "operator: ", operator, "equal_clicked: ", equal_clicked, "result: ", result,"\n")


    # foi clicado 2 vees ou mais consecutivamente
    if equal_clicked == True:
        # primeiro elemento de operanting vai receber o ultimo elemento de results
        operanting [0] = results[-1]
        make_operation(display)
        expression("=", expr)
        equal_clicked = True
        

        print("\n igual depois")
        print("\n", "operanting: ", operanting, "results: ", results, "operator: ", operator, "equal_clicked: ", equal_clicked, "result: ", result,"\n")

        
    else:
        num = eval(display.cget("text"))
        set_number(num)
        make_operation(display)
        expression("=", expr)
        equal_clicked = True
        print("\n igual depois")
        print("\n", "operanting: ", operanting, "results: ", results, "operator: ", operator, "equal_clicked: ", equal_clicked, "result: ", result,"\n")

        


