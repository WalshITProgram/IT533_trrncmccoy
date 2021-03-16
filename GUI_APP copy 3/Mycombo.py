from tkinter import *

class TextFont(Entry):

    def __init__(self, passed_window=None, text_variable="", passed_row=0, passed_column=0, 
                passed_rowspan=1, passed_columnspan=1, passed_sticky=NSEW, passed_args):
        Entry.__init__(self, passed_window, relief=RIDGE, width=20, height=1)
        self.grid(row=passed_row, column=passed_column, rowspan=passed_rowspan, columnspan=passed_column, sticky=passed_sticky)
        self.insert(END, passed_labelText )
        self.config(state=DISABLED, font="Arial")
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

    def listbox2(self):
        scroll = Scrollbar(self.app_screen, orient=VERTICAL)
        scroll.grid(row=4, column=2, sticky=N+S+W)
        self.supported_type_event = Listbox(self.app_screen, relief=SUNKEN, yscrollcommand=scroll.set, selectmode=MULTIPLE)
        self.supported_type_event.grid(row=4,column=2)
        list_index1 = 0 
        for listitem1 in self.listBoxFileTypeVars:
            self.my_list.insert(list_index1, listitem1)
            list_index1 = list_index1 + 1
        scroll.config(command=self.my_list.yview)
