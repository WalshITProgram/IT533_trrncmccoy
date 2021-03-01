from tkinter import *
class EntryFont(Entry):

    def __init__(self, passed_window=None, passed_labelText="", passed_row=0, passed_column=0, 
                passed_rowspan=1, passed_columnspan=1, passed_sticky=NSEW ):
        Entry.__init__(self, passed_window, relief=RIDGE, width=20, height=1)
        self.grid(row=passed_row, column=passed_column, rowspan=passed_rowspan, columnspan=passed_column, sticky=passed_sticky)
        self.insert(END, passed_labelText )
        self.config(state=DISABLED, font="Arial")