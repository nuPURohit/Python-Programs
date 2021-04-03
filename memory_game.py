from tkinter import *
import random
import time
from tkinter import messagebox

data = ["A", "B", "C", "D", "E", "F"]
data_length = len(data)

game_end = 0

dict_cards = {}

clicked_cards = 0

fst_ = ""

scnd_ = ""

start = time.time()

window = Tk()
window.resizable(False, False)
window.title("Memory Game")

f1 = Frame(window)
f1.pack()

bt1 = Button(f1,  width="5", height="3", command=lambda: bttn_clicked(bt1))
bt1.grid(row=0, column=0, padx=20, pady=40)
dict_cards[bt1] = ""

bt2 = Button(f1,  width="5", height="3", command=lambda: bttn_clicked(bt2))
bt2.grid(row=0, column=1, padx=20, pady=40)
dict_cards[bt2] = ""

bt3 = Button(f1,  width="5", height="3", command=lambda: bttn_clicked(bt3))
bt3.grid(row=0, column=2, padx=20, pady=40)
dict_cards[bt3] = ""

bt4 = Button(f1,  width="5", height="3", command=lambda: bttn_clicked(bt4))
bt4.grid(row=0, column=3, padx=20, pady=40)
dict_cards[bt4] = ""

f2 = Frame(window)
f2.pack()

bt5 = Button(f2, width="5", height="3", command=lambda: bttn_clicked(bt5))
bt5.grid(row=1, column=0, padx=20, pady=40)
dict_cards[bt5] = ""

bt6 = Button(f2,  width="5", height="3", command=lambda: bttn_clicked(bt6))
bt6.grid(row=1, column=1, padx=20, pady=40)
dict_cards[bt6] = ""

bt7 = Button(f2,  width="5", height="3", command=lambda: bttn_clicked(bt7))
bt7.grid(row=1, column=2, padx=20, pady=40)
dict_cards[bt7] = ""

bt8 = Button(f2,  width="5", height="3", command=lambda: bttn_clicked(bt8))
bt8.grid(row=1, column=3, padx=20, pady=40)
dict_cards[bt8] = ""

f3 = Frame(window)
f3.pack()

bt9 = Button(f3,  width="5", height="3", command=lambda: bttn_clicked(bt9))
bt9.grid(row=1, column=0, padx=20, pady=40)
dict_cards[bt9] = ""

bt10 = Button(f3,  width="5", height="3", command=lambda: bttn_clicked(bt10))
bt10.grid(row=1, column=1, padx=20, pady=40)
dict_cards[bt10] = ""

bt11 = Button(f3,  width="5", height="3", command=lambda: bttn_clicked(bt11))
bt11.grid(row=1, column=2, padx=20, pady=40)
dict_cards[bt11] = ""

bt12 = Button(f3, width="5", height="3", command=lambda: bttn_clicked(bt12))
bt12.grid(row=1, column=3, padx=20, pady=40)
dict_cards[bt12] = ""

def random_text():
    occurances = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    for bttn in dict_cards:
        if len(data) > 0:
            random.shuffle(data)
            x = data[0]
            dict_cards[bttn] = x
            occurances[x] = occurances[x] + 1

            if occurances[x] == 2:
                data.remove(x)

def bttn_clicked(btn):
    global clicked_cards
    global fst_
    global scnd_

    clicked_cards = clicked_cards + 1

    if clicked_cards == 1:
        fst_ = btn
        btn.configure(text=dict_cards[btn], state=DISABLED)

    if clicked_cards == 2:
        scnd_ = btn
        btn.configure(text=dict_cards[btn], state=DISABLED)

        window.after(500, check_same)

def check_same():
    global clicked_cards
    global fst_
    global scnd_
    global game_end
    global data_length

    if scnd_['text'] != fst_['text']:
        fst_.configure(text="", state="normal")
        scnd_.configure(text="", state="normal")
    else:
        game_end = game_end + 1

    if game_end == data_length:
        messagebox.showinfo("MEMORY GAME", "You have spent " + str(int(time.time() - start)) + " sec!")
        window.destroy()

    clicked_cards = 0
random_text()

window.mainloop()
