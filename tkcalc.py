#!/usr/bin/env python3

from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

root = Tk()

root.geometry("600x600")
root.mainloop()
