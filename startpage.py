
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

import addword
import mydictionary

class startpage:
    def fire1(self):
        obj=addword.addword()
    def fire2(self):
        obj=mydictionary.mydictionary()

    def __init__(self):
        self.root=Tk()
        self.root.geometry("1800x800")

        self.mymenu = Menu(self.root)
        self.root.title("Menu Window")
        self.root.config(menu=self.mymenu)

        submenu1 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage Dictionary", menu=submenu1)
        submenu1.add_command(label="Add New Word" ,command=self.fire1)
        submenu1.add_command(label="View All Words",command=self.fire2)

        self.root.mainloop()
#-------------------------------------------------
startpage()