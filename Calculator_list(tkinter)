from tkinter import *
def clickedChoice():
    z = str(listbox.get(listbox.curselection()))
    x = int(txtNum1.get())
    y = int(txtNum2.get())
    if z == 'Add':
        z = x + y
    if z == 'Sub':
        z = x - y
    if z == 'Mul':
        z = x * y
    if z == 'Div':
        z = x / y
    entryText.set(str(z))


window = Tk()
window.title('List Calculator')
window.geometry("400x250")
var = IntVar()
entryText = StringVar(window)

lblNum1= Label(window,text = "No.1")
lblNum1.grid(row = 0, column = 0)
txtNum1 = Entry(window)
txtNum1.grid(row = 0, column = 1)

lblNum2= Label(window,text = "No.2")
lblNum2.grid(row = 0, column = 2)
txtNum2 = Entry(window)
txtNum2.grid(row = 0, column = 3)

lblChoice = Label(window,text = "Choice").grid(row = 1, column = 0)
listbox = Listbox(window)
listbox.insert(1, "Add")
listbox.insert(2, "Sub")
listbox.insert(3, "Mul")
listbox.insert(4, "Div")

listbox.grid(row = 1, column = 2)

btnSubmit = Button(window, text = "Submit",command=clickedChoice).grid(row = 2, column = 0)
lblAns = Label(window,text = "Ans").grid(row = 3, column = 0)
txtAns = Entry(window,textvariable = entryText).grid(row = 3, column = 1)
window.mainloop()
