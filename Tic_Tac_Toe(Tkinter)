from tkinter import *

turn = 1
def clickedbtn1():
    global turn
    if turn % 2!=0:
         btn1['text']='X'
    else:
        btn1['text']='O'
    turn=turn+1
    winner()
def clickedbtn2():
    global turn
    if turn % 2 != 0:
        btn2['text'] = 'X'
    else:
        btn2['text'] = 'O'
    turn = turn + 1
    winner()
def clickedbtn3():
    global turn
    if turn % 2 != 0:
        btn3['text'] = 'X'
    else:
        btn3['text'] = 'O'
    turn = turn + 1
    winner()
def clickedbtn4():
    global turn
    if turn % 2 != 0:
        btn4['text'] = 'X'
    else:
        btn4['text'] = 'O'
    turn = turn + 1
    winner()
def clickedbtn5():
    global turn
    if turn % 2 != 0:
        btn5['text'] = 'X'
    else:
        btn5['text'] = 'O'
    turn = turn + 1
    winner()
def clickedbtn6():
    global turn
    if turn % 2 != 0:
        btn6['text'] = 'X'
    else:
        btn6['text'] = 'O'
    turn = turn + 1
    winner()
def clickedbtn7():
    global turn
    if turn % 2 != 0:
        btn7['text'] = 'X'
    else:
        btn7['text'] = 'O'
    turn = turn + 1
    winner()
def clickedbtn8():
    global turn
    if turn % 2 != 0:
        btn8['text'] = 'X'
    else:
        btn8['text'] = 'O'
    turn = turn + 1
    winner()
def clickedbtn9():
    global turn
    if turn % 2 != 0:
        btn9['text'] = 'X'
    else:
        btn9['text'] = 'O'
    turn = turn + 1
    winner()
window = Tk()
window.title('tic tac toe')
window.geometry("150x150")
entryText=StringVar(window)

btn1 = Button(window, text = " ",command=clickedbtn1)
btn1.grid(row = 0, column = 0)
btn2 = Button(window, text = " ",command=clickedbtn2)
btn2.grid(row = 0, column = 1)
btn3 = Button(window, text = " ",command=clickedbtn3)
btn3.grid(row = 0, column = 2)
btn4 = Button(window, text = " ",command=clickedbtn4)
btn4.grid(row = 1, column = 0)
btn5 = Button(window, text = " ",command=clickedbtn5)
btn5.grid(row = 1, column = 1)
btn6 = Button(window, text = " ",command=clickedbtn6)
btn6.grid(row = 1, column = 2)
btn7 = Button(window, text = " ",command=clickedbtn7)
btn7.grid(row = 2, column = 0)
btn8 = Button(window, text = " ",command=clickedbtn8)
btn8.grid(row = 2, column = 1)
btn9 = Button(window,text = " ",command=clickedbtn9)
btn9.grid(row = 2,column =2)

def winner():
    if btn1['text'] == btn2['text'] and btn2['text'] == btn3['text']:
        if btn1['text'] == 'X':
            entryText.set('Player 1 has won!')
        elif btn1['text'] == 'O':
            entryText.set('Player 2 has won!')
    if btn4['text'] == btn5['text'] and btn5['text'] == btn6['text']:
        if btn4['text'] == 'X':
            entryText.set('Player 1 has won!')
        elif btn4['text'] == 'O':
            entryText.set('Player 2 has won!')
    if btn7['text'] == btn8['text'] and btn8['text'] == btn9['text']:
        if btn7['text'] == 'X':
            entryText.set('Player 1 has won!')
        elif btn7['text'] == 'O':
            entryText.set('Player 2 has won!')
    if btn1['text'] == btn4['text'] and btn4['text'] == btn7['text']:
        if btn1['text'] == 'X':
            entryText.set('Player 1 has won!')
        elif btn1['text'] == 'O':
            entryText.set('Player 2 has won!')
    if btn2['text'] == btn5['text'] and btn5['text'] == btn8['text']:
        if btn2['text'] == 'X':
            entryText.set('Player 1 has won!')
        elif btn2['text'] == 'O':
            entryText.set('Player 2 has won!')
    if btn3['text'] == btn6['text'] and btn6['text'] == btn9['text']:
        if btn3['text'] == 'X':
            entryText.set('Player 1 has won!')
        elif btn3['text'] == 'O':
            entryText.set('Player 2 has won!')
    if btn1['text'] == btn5['text'] and btn5['text'] == btn9['text']:
        if btn1['text'] == 'X':
            entryText.set('Player 1 has won!')
        elif btn1['text'] == 'O':
            entryText.set('Player 2 has won!')
    if btn3['text'] == btn5['text'] and btn5['text'] == btn7['text']:
        if btn3['text'] == 'X':
            entryText.set('Player 1 has won!')
        elif btn3['text'] == 'O':
            entryText.set('Player 2 has won!')
    if turn>9:
        entryText.set('Tie')

lblwinner = Label(window,text = "Result")
lblwinner.grid(row =3, column =0)
txtans = Entry(window,textvariable=entryText)
txtans.grid(row = 3,column = 1)

window.mainloop()
