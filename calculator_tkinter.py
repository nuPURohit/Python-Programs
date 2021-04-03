from tkinter import *
window = Tk()
window.geometry("312x324")

window.resizable(0, 0)
window.title("CALCULATOR")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""
expression = ""
input_text = StringVar()

input_frame = Frame(window, width = 312, height = 50)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, textvariable = input_text, width = 50)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(window, width = 312, height = 272.5)
btns_frame.pack()

clear = Button(btns_frame, text = "Clear", width = 32, height = 3,command = lambda: btn_clear())
clear.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/",  width = 10, height = 3,command = lambda: btn_click("/"))
divide.grid(row = 0, column = 3, padx = 1, pady = 1)
seven = Button(btns_frame, text = "7",  width = 10, height = 3,command = lambda: btn_click(7))
seven.grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8",  width = 10, height = 3,command = lambda: btn_click(8))
eight.grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9",  width = 10, height = 3, command = lambda: btn_click(9))
nine.grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*",  width = 10, height = 3, command = lambda: btn_click("*"))
multiply.grid(row = 1, column = 3, padx = 1, pady = 1)
four = Button(btns_frame, text = "4",  width = 10, height = 3,command = lambda: btn_click(4))
four.grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5",  width = 10, height = 3,command = lambda: btn_click(5))
five.grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6",  width = 10, height = 3,command = lambda: btn_click(6))
six.grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-",  width = 10, height = 3,command = lambda: btn_click("-"))
minus.grid(row = 2, column = 3, padx = 1, pady = 1)
one = Button(btns_frame, text = "1",  width = 10, height = 3,command = lambda: btn_click(1))
one.grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2",  width = 10, height = 3,command = lambda: btn_click(2))
two.grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", width = 10, height = 3,command = lambda: btn_click(3))
three.grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", width = 10, height = 3,command = lambda: btn_click("+"))
plus.grid(row = 3, column = 3, padx = 1, pady = 1)
zero = Button(btns_frame, text = "0",  width = 21, height = 3,command = lambda: btn_click(0))
zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", width = 10, height = 3,command = lambda: btn_click("."))
point.grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=",  width = 10, height = 3,command = lambda: btn_equal())
equals.grid(row = 4, column = 3, padx = 1, pady = 1)

window.mainloop()
