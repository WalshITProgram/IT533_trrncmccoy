import json
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import *
from tkinter import *
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
        self.servercombo.get()
        settings = {}
        settings["debugMode"] = self.LogFile.get()
        settings["event"] = roles
        settings["file_types"] = filing
        settings["Maxthread"] = self.combo1.get()
        settings["serverPort"] = self.servercombo.get()
        if savefile:
            with open(savefile) as my_file:
                dict_to_open = json.load(my_file)
                for index in settings:
                    s = json.dumps(settings)
                    json.dump(settings, fp=open("file1.json", 'w'), indent = 4)
                    json_file = open("file1.json")
                    print(open("file1.json").read())
                    json_file.close()
                    break
















'''
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

self.file_tp = [{"label": ".doc", "bindVar": self.doc},
                {"label": ".docx", "bindVar": self.docx}, 
                {"label": ".pptx", "bindVar": self.pptx}, 
                {"label": ".xls", "bindVar": self.xls}, 
                {"label": ".xslx", "bindVar": self.xslx}
                {"label": ".rtf", "bindVar": self.rtf}, 
                {"label": ".pdf", "bindVar": self.pdf}, 
                {"label": ".txt", "bindVar": self.txt}, 
                {"label": ".jpg", "bindVar": self.jpg}
                {"label": ".png", "bindVar": self.png}, 
                {"label": ".gif", "bindVar": self.gif}, 
                {"label": ".xml", "bindVar": self.xml}, 
                {"label": ".html", "bindVar": self.html}
                {"label": ".zip", "bindVar": self.zip}, 
                {"label": ".mp4", "bindVar": self.mp4}, 
                {"label": ".mov", "bindVar": self.mov}]

def typecheckbox(self):
    col_count = 2
    for checkBox in self.file_tp:
        Checkbutton(self.app_screen, text=checkBox["label"], variable=checkBox["bindVar"]).grid(row=4, column=col_count, sticky=NSEW)
        col_count = col_count + 1

    for checkBox in self.checkBoxVars:
        filetype = open("/Users/terrancemccoy/IT_533_trrncmcco/IT533_trrncmcco/GUI_APP/file1.json")
        dict_to_open = json.load(filetype) 

        if dict_to_open['file_types'] in checkBox:
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






















def getFile(*args):
    file_type = ""
    comboBoxVal = ttk.Combobox()
    comboBoxItems = [ ".doc", ".docx", ".pptx", ".xls", ".xslx", 
                      ".rtf", ".pdf", ".txt", ".jpg", ".png", ".gif", 
                      ".xml", ".html", ".zip", ".mp4", ".mov"]

    filetype = open("/Users/terrancemccoy/IT_533_trrncmcco/IT533_trrncmcco/GUI_APP/file1.json")
    dict_to_open = json.load(filetype)    

 def getFile(self, *args):
        openfile = askopenfilename()
        self.LogFile.get()
        roles 
        self.comboBoxVal.get()
        self.combo1.get()
        self.servercombo.get()
        settings = {}
        settings["debugMode"] = self.LogFile.get()
        settings["event"] = roles
        settings["file_types"] = self.comboBoxVal.get()
        settings["Maxthread"] = self.combo1.get()
        settings["serverPort"] = self.servercombo.get()
        if openfile:
            with open(openfile) as my_file:
                dict_to_open = json.load(my_file)
                for index in settings:
                    s = json.dumps(settings)
                    json.dump(settings, fp=open("file1.json", 'w'), indent = 4)
                    json_file = open("file1.json")
                    print(open("file1.json").read())
                    json_file.close()	
	

    






getFile()



    for index in comboBoxItems:
        if dict_to_open['Help_Desk'][0]['file_types'][0] in index or dict_to_open['Help_Desk'][0]['file_types'][1] in index:
            _file_types_doc = dict_to_open['Help_Desk'][0]['file_types'] 
            print(_file_types_doc)
            break
    for index in comboBoxItems:
        if dict_to_open['Help_Desk'][1]['file_types'][0] in index or dict_to_open['Help_Desk'][1]['file_types'][1] in index:
            file_types_ppt = dict_to_open['Help_Desk'][1]['file_types']
            print(file_types_ppt)
            break
    for index in comboBoxItems:
        if dict_to_open['Help_Desk'][2]['file_types'][0] in index or dict_to_open['Help_Desk'][2]['file_types'][1] in index:
            file_types_txt = dict_to_open['Help_Desk'][2]['file_types']
            print(file_types_txt)
            break
     
filetype = open("/Users/terrancemccoy/IT_533_trrncmcco/IT533_trrncmcco/GUI_APP/file1.json")
dict_to_open = json.load(filetype)
if dict_to_open['Help_Desk'][0]['file_types'][0] or dict_to_open['Help_Desk'][0]['file_types'][1]:
    _file_types_doc = dict_to_open['Help_Desk'][0]['file_types']
    print(_file_types_doc)

filetype = open("/Users/terrancemccoy/IT_533_trrncmcco/IT533_trrncmcco/GUI_APP/file1.json")
dict_to_open = json.load(filetype)
if dict_to_open['Help_Desk'][1]['file_types'][0] or dict_to_open['Help_Desk'][1]['file_types'][1]:
    file_types_ppt = dict_to_open['Help_Desk'][1]['file_types']
    print(file_types_ppt)

filetype = open("/Users/terrancemccoy/IT_533_trrncmcco/IT533_trrncmcco/GUI_APP/file1.json")
dict_to_open = json.load(filetype)
if dict_to_open['Help_Desk'][2]['file_types'][0] or dict_to_open['Help_Desk'][2]['file_types'][1]:
    file_types_txt = dict_to_open['Help_Desk'][2]['file_types']
    print(file_types_txt)




    if dict_to_open['Help_Desk'][1]['file_types'] == dict_to_open['Help_Desk'][1]['file_types']:
        supported_file_types = dict_to_open['Help_Desk'][1]['file_types'] 
        print(supported_file_types)
    if dict_to_open['Help_Desk'][1]['file_types'] == dict_to_open['Help_Desk'][1]['file_types']:
        supported_file_types = dict_to_open['Help_Desk'][1]['file_types'] == dict_to_open['Help_Desk'][1]['file_types']
        print(supported_file_types)
    filetype.close()
highlightListboxItemsByIndex()

def Indexitems():
    filetype = open("/Users/terrancemccoy/IT_533_trrncmcco/IT533_trrncmcco/GUI_APP/file1.json")
    dict_to_open = json.load(filetype)
    if dict_to_open['Help_Desk'][0]['file_types'] == dict_to_open['Help_Desk'][0]['file_types']:
        file_types = dict_to_open['Help_Desk'][0]['file_types']
        print(file_types)
    filetype.close()
highlightListboxItemsByIndex()

'''

