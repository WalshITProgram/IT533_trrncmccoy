from tkinter import *
import sys
#from textclass import *
from sys import exit
from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *
from tkinter.messagebox import *
'''
Load Widget Class from tkinter Module
Make an instance of the imported Label Class 
Pack arranges the new label class 
Main Loop brings up window and starts the tkinter event loop
Mainloop monitors events to report back to the callback handler
None Means "attach the new label to the default top level window of this program

'''
class NewMenuDemo(Frame):
    def __init__(self, parent=None, file=None):
        Frame.__init__(self, parent=None)
        self.pack(expand=YES, fill=BOTH)
        self.CreateWidgets()
        self.master.title("Help Desk Menu")


    def CreateWidgets(self):
        self.makeMenuBar()


    def makeMenuBar(self):
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.fileMenu()

    def fileMenu(self):
        pulldown = Menu(self.menubar)
        pulldown.add_command(label='Find File', command=self.onFile)
        pulldown.add_command(label='Open File', command=self.onOpen)
        pulldown.add_command(label='Save File', command=self.onSave)
        pulldown.add_command(label='Quit', command=self.quit)
        self.menubar.add_cascade(label='File', underline=0, menu=pulldown)

    def onFile(self):
        target = askstring('SimpleEditor','Search for File?')
        if target:
            where = self.text.search(target, INSERT, END)

            if where:
                print(where)
                pastit = where + ('+%dc' % len(target))
                self.text.tag_add(SEL, where, pastit)
                self.text.mark_Set(INSERT, pastit)
                self.text.see(INSERT, pastit)
                self.text.focus()
    
    def onSave(self):
        filename = asksaveasfilename()
        if filename:
            all_text = self.gettext()
            open(filename, 'w').write(all_text)

    def onOpen(self):
        filename = askopenfilename()
        if filename:
            all_text = self.gettext()
            open(filename, 'w').write(all_text)


    def quit(self):
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            Frame.quit(self)

    
    
if __name__=='__main__': 
    if len(sys.argv) > 1:
        NewMenuDemo(file=sys.argv[1]).mainloop()
    else:
        NewMenuDemo().mainloop()
        scroll = Scrollbar(self.app_screen, orient=VERTICAL)
        scroll.grid(row=3, column=2, sticky=NSEW)
        self.my_textbox = Text(self.app_screen, relief=SUNKEN, yscrollcommand=scroll.set)
        self.my_textbox.grid(row=6, column=0, sticky=SE)
        scroll.config(command=self.my_textbox)









