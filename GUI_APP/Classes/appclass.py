from tkinter import *
try:
    from Classes.Text_subclass import *
except ImportError:
    pass
#from Classes.Menu import *
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
Create a class called App
Create a constructor
Create variables for checkbox, listbutton and combobox
Create Variables with IntVar() for checkbox 
Create a list of values labeled options 

"""
class App():
    def __init__(self):
        self.app_screen = Tk()
        self.app_screen.geometry("1305x250")
        self.my_box = Text()
        self.LogFile = StringVar()
        self.serverport = IntVar()
        self.max_thread_options = [1, 2, 4]
        self.options = ["off", "on"]
        self.my_list = Listbox()
        self.appcheckbox = IntVar()
        self.seccheckbox = IntVar()
        self.errorcheckbox = IntVar()
        self.incheckbox = IntVar() 
        self.outcheckbox = IntVar()
        self.doc = IntVar()
        self.docx = IntVar()
        self.pptx = IntVar() 
        self.xls = IntVar()
        self.xslx = IntVar()
        self.rtf = IntVar()
        self.pdf = IntVar()
        self.txt = IntVar()
        self.jpg = IntVar()
        self.png = IntVar()
        self.gif = IntVar()
        self.xml = IntVar()
        self.html = IntVar()
        self.zip = IntVar()
        self.mp4 = IntVar()
        self.mov = IntVar()

# Create a list of variables and bind them to the labels
# Inside the dictionary create key called labeled
# Create another key labled bindvar with the file type variable

        self.file_tp = [{"label": ".doc", "bindVar": self.doc},
                        {"label": ".docx", "bindVar": self.docx}, 
                        {"label": ".pptx", "bindVar": self.pptx}, 
                        {"label": ".xls", "bindVar": self.xls}, 
                        {"label": ".xslx", "bindVar": self.xslx},
                        {"label": ".rtf", "bindVar": self.rtf}, 
                        {"label": ".pdf", "bindVar": self.pdf}, 
                        {"label": ".txt", "bindVar": self.txt}, 
                        {"label": ".jpg", "bindVar": self.jpg},
                        {"label": ".png", "bindVar": self.png}, 
                        {"label": ".gif", "bindVar": self.gif}, 
                        {"label": ".xml", "bindVar": self.xml}, 
                        {"label": ".html", "bindVar": self.html},
                        {"label": ".zip", "bindVar": self.zip}, 
                        {"label": ".mp4", "bindVar": self.mp4}, 
                        {"label": ".mov", "bindVar": self.mov}]

        self.checkBoxVars = [{"label": "Application", "bindVar": self.appcheckbox},
                             {"label": "Security", "bindVar": self.seccheckbox}, 
                             {"label": "Error", "bindVar": self.errorcheckbox}, 
                             {"label": "Input", "bindVar": self.incheckbox}, 
                             {"label": "Sever", "bindVar": self.outcheckbox}]

# Create a combobox for Debug Mode/MaxThread/Server
# Create a list with values 
# Create setup interface

        self.comboboxVa = ttk.Combobox()
        self.comboBoxItem = ["on", "off"]

        self.combo1 = ttk.Combobox()
        self.comboitem = ["1", "2", "4"]

        self.servercombo = ttk.Combobox()
        self.comboserver = ["50000", "50100", "50200", "50300", "50300", " 50400", "50500"]

        self.setupInterface()

# Create a functions to set up on the help desk menu called combo/combo5/comboserver1/typecheckbox
# If a user clicks on the item it should add value to json file
# Declare readonly to prevent changes 

    def combo(self):
        self.comboboxVa = ttk.Combobox(self.app_screen, state="readonly", values=self.comboBoxItem)
        self.comboboxVa.grid(row=5, column=2, sticky=NSEW)
        self.comboboxVa.current()

    def combo5(self):
        self.combo1 = ttk.Combobox(self.app_screen, state="readonly", values=self.comboitem)
        self.combo1.grid(row=1, column=2, sticky=NSEW)
        self.combo1.current(0)

    def comboserver1(self):
        self.servercombo = ttk.Combobox(self.app_screen, state="readonly", values=self.comboserver)
        self.servercombo.grid(row=6, column=2, sticky=NSEW)
        self.servercombo.current(0)

    def typecheckbox(self):
        col_count = 2
        for checkBox in self.file_tp:
            Checkbutton(self.app_screen, text=checkBox["label"], variable=checkBox["bindVar"]).grid(row=4, column=col_count, sticky=NSEW)
            col_count = col_count + 1
            
# Create checkbox list the values in horizontal row
# Open json file to add values inside the keys
# Create a for loop inside the checkboxVars to iterate to variable 
# Create a dictionary to locate the proper index inside the json file

    def filecheckbox(self):
        col_count = 2
        for checkBox in self.checkBoxVars:
            Checkbutton(self.app_screen, text=checkBox["label"], variable=checkBox["bindVar"]).grid(row=3, column=col_count, sticky=NSEW)
            col_count = col_count + 1

        for checkBox in self.checkBoxVars:
            filetype = open("/Users/terrancemccoy/IT_533_trrncmcco/IT533_trrncmcco/GUI_APP/file2.json")
            dict_to_open = json.load(filetype) 

            if dict_to_open['event'] in checkBox:
                _file_types_doc = dict_to_open['event']

        for checkBox in self.checkBoxVars:
            if dict_to_open['event'] in checkBox:
                file_types_ppt = dict_to_open['event']

        for checkBox in self.checkBoxVars:
            if dict_to_open['event']in checkBox:
                file_types_txt = dict_to_open['event']
        
        for checkBox in self.checkBoxVars:
            if dict_to_open['event']in checkBox:
                file_types_txt = dict_to_open['event']

# Create a getfile function
# askopenfilename to load the json file with the preset configurations
# Create a empty variable and create get() to retrieve the values

    def getFile(self, *args):
        openfile = askopenfilename()        
        filing = ""
        if self.doc.get() == 1:
            filing = filing + ".doc"

        if self.docx.get() == 1:
            filing = filing + ".docx"

        if self.pptx.get() == 1:
            filing = filing + ".pptx"

        if self.xls.get() == 1:
            filing = filing + ".xls"

        if self.xslx.get() == 1:
            filing = filing + ".xslx"

        if self.rtf.get() == 1:
            filing =  filing + ".rtf"

        if self.pdf.get() == 1:
            filing = filing + ".pdf"

        if self.txt.get() == 1:
            filing = filing + ".txt"

        if self.jpg.get() == 1:
            filing = filing + ".jpg"

        if self.png.get() == 1:
            filing = filing + ".png"

        if self.gif.get() == 1:
            filing = filing + ".gif"

        if self.xml.get() == 1:
            filing = filing + ".xml"

        if self.html.get() == 1:
            filing = filing + ".html"

        if self.zip.get() == 1:
            filing = filing + ".zip"

        if self.mp4.get() == 1:
            filing = filing + ".mp4"

        if self.mov.get() == 1:
            filing = filing + ".mov"

# Append the values to the index inside the roles variable

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

# Create dict and values to the proper index 

        settings = {}
        settings["Logfile"] = self.LogFile.get()
        settings["debugMode"] = self.comboboxVa.get()
        settings["event"] = roles
        settings["file_types"] = filing
        settings["Maxthread"] = self.combo1.get()
        settings["serverPort"] = self.servercombo.get()
# After the variables are attained use the get() to add it to the settings dict 
        self.LogFile.get()
        roles 
        filing
        self.combo1.get()
        self.comboboxVa.get()
        self.servercombo.get()

# Create a function to open the json file and set the variables to the correct index
        if openfile:
            with open(openfile) as myfile:
                setting = json.load(myfile)
                print(setting)
                self.combo1.set(settings["Maxthread"])
                self.LogFile.set(settings["Logfile"])
                self.comboboxVa.set(settings["debugMode"])
                self.servercombo.set(settings["serverPort"])
   
# Same process as the last function except that this save the file to file2.json

    def saveFile(self, *args):
        savefile = asksaveasfile()
        filing = ""
        if self.doc.get() == 1:
            filing = filing + ".doc"

        if self.docx.get() == 1:
            filing = filing + ".docx"

        if self.pptx.get() == 1:
            filing = filing + ".pptx"

        if self.xls.get() == 1:
            filing = filing + ".xls"

        if self.xslx.get() == 1:
            filing = filing + ".xslx"

        if self.rtf.get() == 1:
            filing =  filing + ".rtf"

        if self.pdf.get() == 1:
            filing = filing + ".pdf"

        if self.txt.get() == 1:
            filing = filing + ".txt"

        if self.jpg.get() == 1:
            filing = filing + ".jpg"

        if self.png.get() == 1:
            filing = filing + ".png"

        if self.gif.get() == 1:
            filing = filing + ".gif"

        if self.xml.get() == 1:
            filing = filing + ".xml"

        if self.html.get() == 1:
            filing = filing + ".html"

        if self.zip.get() == 1:
            filing = filing + ".zip"

        if self.mp4.get() == 1:
            filing = filing + ".mp4"

        if self.mov.get() == 1:
            filing = filing + ".mov"

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

        self.LogFile.get()
        roles 
        filing
        self.combo1.get()
        self.comboboxVa.get()
        self.servercombo.get()

        settings = {}
        settings["Logfile"] = self.LogFile.get()
        settings["debugMode"] = self.comboboxVa.get()
        settings["event"] = roles
        settings["file_types"] = filing
        settings["Maxthread"] = self.combo1.get()
        settings["serverPort"] = self.servercombo.get()

        if savefile:
            for index in settings:
                s = json.dumps(settings)
                json.dump(settings, fp=open("file2.json", 'w'), indent = 4)
                json_file = open("file2.json")
                print(open("file2.json").read())
                json_file.close()
                break 
# Create a quit function to exit system 

    def quit(self):
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            self.app_screen.destroy()

# Grid will help you design the GUI app layout 
# Create 6 text labels and place the functions underneath the Text_label functions

    def setupGrid(self):
        text_label = TextFont(self.app_screen, "Max Threads:", 1, 1, 1, 2)
        self.combo5()

        text_label1 = TextFont(self.app_screen, "Event Log File Location", 2, 1, 1, 2)
        self.file_location = Entry(self.app_screen, textvariable=self.LogFile)
        self.file_location.grid(row=2, column=2, sticky=NSEW)

        text_label2 = TextFont(self.app_screen, "Types of Events to Log:", 3, 1, 1, 2)
        self.filecheckbox()
        
        text_label3 = TextFont(self.app_screen, "Supported File Types:", 4, 1, 1, 2)
        self.typecheckbox()

        text_label4 = TextFont(self.app_screen, "Debug Mode",  5, 1, 1, 2)
        self.combo()

        text_label5 = TextFont(self.app_screen, "Server Port #:", 6, 1, 1, 2 )
        self.comboserver1()

        submitButton = Button(self.app_screen, text="Submit")
        submitButton.grid(row=8, column=2, sticky=NSEW)
        submitButton.bind("<Button-1>", self.submitData)

        loadButton = Button(self.app_screen, text= "Load")
        loadButton.grid(row=8, column=1, sticky=NSEW) 
        loadButton.bind("<Button-1>", self.getFile)
# Create Menu and add commands to the menu such as load and save settings 
    def Menu(self):
        topMenu = Menu(self.app_screen)
        self.app_screen.config(menu=topMenu)
        jfile = Menu(topMenu)
        jfile.add_command(label='Load Settings from JSON', command=self.getFile, accelerator="Ctrl+1")
        jfile.add_command(label='Save Settings to JSON', command=self.saveFile, accelerator="Ctrl+s")
        jfile.add_command(label='Quit', command=self.quit)
        topMenu.add_cascade(label='Config Settings', menu=jfile)
        self.app_screen.bind_all("<Control-1>", self.getFile)
        self.app_screen.bind_all("<Control-s>", self.submitData)

# Interface lets you design the layout and structure of the GUI APP 

    def setupInterface(self):
        self.app_screen.title("Help Desk Menu")
        self.Menu()
        self.setupGrid()
        self.app_screen.mainloop()

# Create a sumbitdata function to obtain the information from get()
    def submitData(self, *passed_args):
        filing = ""
        if self.doc.get() == 1:
            filing = filing + ".doc"

        if self.docx.get() == 1:
            filing = filing + ".docx"

        if self.pptx.get() == 1:
            filing = filing + ".pptx"

        if self.xls.get() == 1:
            filing = filing + ".xls"

        if self.xslx.get() == 1:
            filing = filing + ".xslx"

        if self.rtf.get() == 1:
            filing =  filing + ".rtf"

        if self.pdf.get() == 1:
            filing = filing + ".pdf"

        if self.txt.get() == 1:
            filing = filing + ".txt"

        if self.jpg.get() == 1:
            filing = filing + ".jpg"

        if self.png.get() == 1:
            filing = filing + ".png"

        if self.gif.get() == 1:
            filing = filing + ".gif"

        if self.xml.get() == 1:
            filing = filing + ".xml"

        if self.html.get() == 1:
            filing = filing + ".html"

        if self.zip.get() == 1:
            filing = filing + ".zip"

        if self.mp4.get() == 1:
            filing = filing + ".mp4"

        if self.mov.get() == 1:
            filing = filing + ".mov"
 
 # Retrieve the values from the appcheckbox and assign it to the roles variable 

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

        self.LogFile.get()
        roles 
        filing
        self.comboboxVa.get()
        self.combo1.get()
        self.servercombo.get()
  
        settings = {}
        settings["debugMode"] = self.comboboxVa.get()
        settings["Logfile"] = self.LogFile.get()
        settings["event"] = roles
        settings["file_types"] = filing
        settings["Maxthread"] = self.combo1.get()
        settings["serverPort"] = self.servercombo.get()
# Open json file and save the settings to the file
        for index in settings:
            s = json.dumps(settings)
            json.dump(settings, fp=open("file1.json", 'w'), indent = 4)
            json_file = open("file1.json")
            print(open("file1.json").read())
            json_file.close()
            break	


    

    
   







