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
        self.my_box = Text()
        self.user = StringVar()
        self.appcheckbox = IntVar()
        self.seccheckbox = IntVar()
        self.errorcheckbox = IntVar()
        self.incheckbox = IntVar() 
        self.outcheckbox = IntVar()
        self.my_list = Listbox()
        self.comboBoxVal = ttk.Combobox()
        self.comboBoxItems = [ ".doc", ".docx", ".pptx", ".xls", ".xslx", 
                             ".rtf", ".pdf", ".txt", ".jpg", ".png", ".gif", 
                             ".xml", ".html", ".zip", ".mp4", ".mov"]
  
        self.checkBoxVars = [{"label": "Application", "bindVar": self.appcheckbox},
                             {"label": "Security", "bindVar": self.seccheckbox}, 
                             {"label": "Error", "bindVar": self.errorcheckbox}, 
                             {"label": "Input", "bindVar": self.incheckbox}, 
                             {"label": "Output", "bindVar": self.outcheckbox}]
        self.setupInterface()

    def combobox(self):
        self.comboBoxVal = ttk.Combobox(self.app_screen, state="readonly", values=self.comboBoxItems)
        self.comboBoxVal.grid(row=8, column=1, sticky=NSEW)
        self.comboBoxVal.current(0)


    def filecheckbox(self):
        row_count = 1
        for checkBox in self.checkBoxVars:
            Checkbutton(self.app_screen, text=checkBox["label"], variable=checkBox["bindVar"]).grid(row=row_count, column=1, sticky=NSEW)
            row_count = row_count + 1
    
    def memory_options(self, *args):

        with open("GUI_APP/file1.json") as f:
            data = json.load(f)

    def getFile(self, *args):
        openfile = askopenfilename()

        if openfile:
            with open(openfile) as my_file:
                file_contents = my_file.read()
                config_vars =json.load(my_file)
                self.comboBoxVal = ttk.Combobox(self.app_screen, values=self.memory_options)
                self.comboBoxVal.grid(row=4, column=1, sticky=NSEW)
                self.comboBoxVal.current(self.memory_options.index(config_vars["eventType"]))
                logField = Entry(self.app_screen)
                logField.grid(row=4, column=1, sticky=NSEW)
                logField.insert(0, config_vars["log"])
   

    def onFile(self):
        target = askstring('SimpleEditor','Search for File?')
        if target:
                filename = filedialog.askopenfilename(initialdir = "/Users/terrancemccoy/IT_533_trrncmcco/IT533_trrncmcco",
                                          title = "Select a File",
                                          filetypes = (("GUI",
                                                        "*.py*"),
                                                       ("all files",
                                                        "*.*")))

    
    def onSave(self):
        files = [('/Users/terrancemccoy/IT_533_trrncmcco/IT533_trrncmcco', '*.*'),  
        ('GUI', '*.py')] 
        file = asksaveasfile(filetypes = files, defaultextension = files) 


    def quit(self):
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            self.app_screen.destroy()

    def setupGrid(self):
        TextFont(self.app_screen, "Name", 0, 1)
        Field = Entry(self.app_screen)
        Field.grid(row=0, column=2, sticky=NSEW)
        Field.config(textvariable=self.user)
        Field.bind("<Return>", self.submitData)
        self.filecheckbox()
        self.combobox()
        submitButton = Button(self.app_screen, text="Submit")
        submitButton.grid(row=8, column=2, sticky=NSEW)
        submitButton.bind("<Button-1>", self.submitData)

    def Menu(self):
        topMenu = Menu(self.app_screen)
        self.app_screen.config(menu=topMenu)
        
        Main_menu = Menu(topMenu)
        Main_menu.add_command(label='Find File', command=self.onFile)
        Main_menu.add_command(label='Open File', command=self.getFile)
        Main_menu.add_command(label='Save File', command=self.onSave)
        Main_menu.add_command(label='Quit', command=self.quit)
        topMenu.add_cascade(label='File', underline=0, menu=Main_menu)
    
    def setupInterface(self):
        self.app_screen.title("Help Desk Menu")
        self.Menu()
        self.setupGrid()
        self.app_screen.mainloop()
    
    def submitData(self, *passed_args):
        roles = ""
        if self.appcheckbox.get() == 1:
            roles = roles + "Application"
        if self.seccheckbox.get() == 1:
            roles = roles + "Security"
        if self.errorcheckbox.get() == 1:
            roles = roles + "Error"
        if self.incheckbox.get() == 1:
            roles = roles + "Input"
        if self.outcheckbox.get() == 1:
            roles = roles + "Output"
  
        
        print(self.user.get() + " " + roles + self.comboBoxVal.get())
        
    def threading(self):
        t1=Thread(target=submitData)
        t1.start()
    

    
   







