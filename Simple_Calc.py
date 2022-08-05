#This is only Basic Level Calculator

# importing Modules
import tkinter as tk
from tkinter import messagebox
import time

# Intializing Varibles
expression = ""

# FunctionS
def equalpress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except Exception:
        equation.set("SyntaxError")
        expression=""

def clear():
    global expression
    expression = ""
    equation.set("0")

def Delchar():
    global expression
    expression=expression[:-1]

def click(ch):
    global expression
    if ch not in ["=","Del","AC"]:
        if (ch == ")") and (expression.count("(") <= expression.count(")")):
            messagebox.showinfo(title = "Error", message = "Invalid Parenthesis")
        else:
            expression += ch
            equation.set(expression)
    elif ch == "=":
        equalpress()
    elif ch == "AC":
        clear()
    elif ch == "Del":
        Delchar()
        equation.set(expression)

if __name__ == '__main__':

    # Initiallizing Window
    root=tk.Tk()
    root.title("CalcPython")
    root.configure(bg = 'Light green')
    root.geometry("320x242")
    root.resizable(False, False)

    # Result and console screen
    equation = tk.StringVar()
    equation.set("0")
    expression_field = tk.Entry(root, textvariable = equation, font = "Helvetica 10 bold", fg = "Green") 
    expression_field.grid(row=0, columnspan = 4, ipadx = 90, ipady = 20)
    

    # BUttons Grid
    tk.Button(root, text = "1", width = 10, command = lambda:click("1"), fg = 'Blue', bg = '#7EF7EE').grid(row = 5, column = 0)
    tk.Button(root, text = "2", width = 10, command = lambda:click("2"), fg = 'Blue', bg = '#7EF7EE').grid(row = 5, column = 1)
    tk.Button(root, text = "3", width = 10, command = lambda:click("3"), fg = 'Blue', bg = '#7EF7EE').grid(row = 5, column = 2)
    tk.Button(root, text = "4", width = 10, command = lambda:click("4"), fg = 'Blue', bg = '#7EF7EE').grid(row = 4, column = 0)
    tk.Button(root, text = "5", width = 10, command = lambda:click("5"), fg = 'Blue', bg = '#7EF7EE').grid(row = 4, column = 1)
    tk.Button(root, text = "6", width = 10, command = lambda:click("6"), fg = 'Blue', bg = '#7EF7EE').grid(row = 4, column = 2)
    tk.Button(root, text = "7", width = 10, command = lambda:click("7"), fg = 'Blue', bg = '#7EF7EE').grid(row = 3, column = 0)
    tk.Button(root, text = "8", width = 10, command = lambda:click("8"), fg = 'Blue', bg = '#7EF7EE').grid(row = 3, column = 1)
    tk.Button(root, text = "9", width = 10, command = lambda:click("9"), fg = 'Blue', bg = '#7EF7EE').grid(row = 3, column = 2)
    tk.Button(root, text = ".", width = 10, command = lambda:click("."), fg = 'Blue', bg = '#7EF7EE').grid(row = 6, column = 3)
    tk.Button(root, text = "0", width = 10, command = lambda:click("0"), fg = 'Blue', bg = '#7EF7EE').grid(row = 6, column = 1)
    tk.Button(root, text = "00", width = 10, command = lambda:click("00"), fg = 'Blue', bg = '#7EF7EE').grid(row = 6, column = 2)
    tk.Button(root, width = 10, command = lambda:click("%"), bg = 'Red').grid(row = 1, column = 0)
    tk.Button(root, text = "/", width = 10, command = lambda:click("/"), fg = 'Brown', bg = '#7EF7EE').grid(row = 2, column = 3)
    tk.Button(root, text = "X", width = 10, command = lambda:click("*"), fg = 'Brown', bg = '#7EF7EE').grid(row = 3, column = 3)
    tk.Button(root, text = "-", width = 10, command = lambda:click("-"), fg = 'Brown', bg = '#7EF7EE').grid(row = 4, column = 3)
    tk.Button(root, text = "+", width = 10, command = lambda:click("+"), fg = 'Brown', bg = '#7EF7EE').grid(row = 5, column =  3)
    tk.Button(root, text = "(", width = 10, command = lambda:click("("), fg = 'Brown', bg = '#7EF7EE').grid(row = 2, column = 0)
    tk.Button(root, text = ")", width = 10, command = lambda:click(")"), fg = 'Brown', bg = '#7EF7EE').grid(row = 2, column = 1)
    tk.Button(root, width = 10, command = lambda:click("//"), bg = 'Red').grid(row = 2,column = 2)
    tk.Button(root, width = 10, command = lambda:click("+/-"), bg = 'Red').grid(row = 6, column = 0)
    tk.Button(root, text = "=", width = 10, command = lambda:click("="), fg = 'Green', bg = '#7EF7EE').grid(row = 1, column = 1)
    tk.Button(root, text = "AC", width = 10, command=lambda:click("AC"), fg = 'Orange', bg = '#7EF7EE').grid(row = 1, column = 2)
    tk.Button(root, text = "Del", width = 10, command=lambda:click("Del"), fg = 'Red', bg = '#7EF7EE').grid(row = 1,column = 3)
    root.mainloop()
