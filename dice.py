#!/usr/bin/env python3

from tkinter import Tk, Button, Label, Entry, Frame
from random import randint
import sys

root = Tk()

def dice():
    print (randint(1,6))

def exit():
    print("Bye Bye!!")
    sys.exit()

header = Label(root, text="Dice App v1.0")
header.pack()

h = Entry(root)
h.pack()
h.focus_set()
 
a = Button(root, text="Roll Dice", width=30, command=dice)
a.pack()

exit = Button(root, text="Exit App", width=30, command=exit)
exit.pack()

root.geometry("300x200")
root.mainloop()
