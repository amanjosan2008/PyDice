#!/usr/bin/env python3
from tkinter import *
from random import randint
import sys

root = Tk()

e = Entry(root, width=10, font=("Helvetica", 30, "bold"), justify=CENTER)
e.pack()

e.delete(0, END)
e.insert(0, "Ready!!")

def dice():
    e.delete(0, END)
    e.insert(0, randint(1,6))

def exit():
    print("Bye Bye!!")
    sys.exit()

header = Label(root, text="Dice App v1.0")
header.pack()

a = Button(root, text="Roll Dice", width=20, command=dice)
a.pack()

f = Button(root, text="Exit App", width=20, fg="Red", command=exit)
f.pack()

root.geometry("280x130")
root.mainloop()
