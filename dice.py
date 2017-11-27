#!/usr/bin/env python3
from tkinter import *
from random import randint
import sys

root = Tk()

def exit():
    print("Bye Bye!!")
    sys.exit()

header = Label(root, text="Dice App v1.0")
header.pack()

e = Entry(root)
e.pack()

e.delete(0, END)
e.insert(0, "Click Roll Dice!!")

def dice():
    e.delete(0, END)
    e.insert(0, randint(1,6))

a = Button(root, text="Roll Dice", width=30, command=dice)
a.pack()

exit = Button(root, text="Exit App", width=30, command=exit)
exit.pack()

root.geometry("300x300")
root.mainloop()

