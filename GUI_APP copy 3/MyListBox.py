from tkinter import *
from Classes.Text_subclass import *
from Classes.Menu import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import *
from tkinter import ttk 
import sys
from sys import exit
from tkinter.simpledialog import *
from tkinter import filedialog
from tkinter.messagebox import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *
from tkinter.messagebox import *
import json
import time
from threading import * 

"""
Create a class for the Help Desk App
Create Constructor with values:
App Screen = Tk function
Set Up Interface:
Title = "Help Desk Menu"
Create a Grid:
"""
class App():
    def __init__(self):
        self.app_screen = Tk()
        self.app_screen.geometry("395x307")
        self.my_box = Text()
        self.LogFile = StringVar()
        self.serverport = IntVar()
        self.max_thread_options = [1, 2, 4]
        self.options = ["off", "on"]
        self.my_list = Listbox()
        self.listBoxEventVars = ["application", "security", "error", "input/output"]
        self.listBoxFileTypeVars =  [".doc", ".docx", ".pptx", ".xls", ".xslx", ".rtf", ".pdf", ".txt", ".jpg", ".png", ".gif", ".xml", ".html", ".zip", ".mp4", ".mov"]
        self.setupInterface()

    def listbox1(self):
        scroll = Scrollbar(self.app_screen, orient=VERTICAL)
        scroll.grid(row=3, column=2, sticky=N+S+W)
        self.type_event = Listbox(self.app_screen, relief=SUNKEN, yscrollcommand=scroll.set, selectmode=MULTIPLE)
        self.type_event.grid(row=3, column=2, sticky=NSEW)
        list_index = 0
        for listitem in self.listBoxEventVars:
            self.my_list.insert(list_index, listitem)
            list_index = list_index + 1
        scroll.config(command=self.my_list.yview)
if __name__=='__main__':
    App().mainloop()