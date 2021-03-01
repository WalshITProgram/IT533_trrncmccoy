from tkinter import *

    def handleList(self, event):
        index = self.listbox.curselection()
        label = self.listbox.get(index)
        self.runCommand(label)

    def make_widgets(self, options):
        sbar = Scrollbar(self)
        lists = Listbox(self, relief=SUNKEN)
        sbar.config(command=lists.yview)
        lists.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        lists.pack(side=LEFT, expand=YES, fill=BOTH)
        pos = 0 
        for label in options:
            lists.insert(pos, label)
            pos += 1
            lists.bind('<Double-1>', self.handleList)
            self.listbox = lists

    def runCommand(self, selection):
        print('You selected:', selection)

Text.__init__(self, parent, file=None)
        
        self.pack(expand=YES, fill=BOTH


    def drawListbox(self):
        Bar = Scrollbar(self.app_screen, orient=VERTICAL)
        Bar.grid(row=1, column=1, sticky=N+S+W)
        self.mylist = Listbox(self.app_screen, relief=SUNKEN, yscrollcommand=Bar.set, selectmode=MULTIPLE)
        self.mylist.grid(row=1, column=0, sticky=NSEW)
        list_index = 0
        for listindex in self.listBoxVars:
            self.mylist.insert(list_index, listindex)
            list_index = list_index + 1
                    Bar.config(command=self.mylist.xview)
                self.appcheckbox = IntVar()
        self.seccheckbox = IntVar()
        self.errorcheckbox = IntVar()
        self.inputcheckbox = IntVar()
        self.checkBoxVars = [{"label": "Application", "bindVar": self.appcheckbox},
                             {"label": "Security", "bindVar": self.seccheckbox},
                             {"label": "Errors", "bindVar": self.errorcheckbox},
                             {"label": "Input", "bindVar": self.inputcheckbox}]
            def CheckBox(self):
        col_count = 0
        for checkbox in self.checkBoxVars:
            Checkbutton(self.app_screen, text=checkbox["label"], 
                        variable=checkbox["bindVar"]).grid(row=2, column=col_count, sticky=NSEW)
            col_count = col_count + 1