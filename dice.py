#!/usr/bin/env python3

from tkinter import *
from random import randint
import sys

root = Tk()

def dice():
    Label(root, text=randint(1,60)).pack()

def exit():
    print("Bye Bye!!")
    sys.exit()

header = Label(root, text="Dice App v1.0")
header.pack()

a = Button(root, text="Roll Dice", width=30, command=dice)
a.pack()

exit = Button(root, text="Exit App", width=30, command=exit)
exit.pack()

root.geometry("300x300")
root.mainloop()

