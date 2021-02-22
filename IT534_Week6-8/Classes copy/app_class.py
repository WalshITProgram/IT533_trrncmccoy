from tkinter import *
from Classes.text import *
from tkinter import ttk 

class APP():

    def __init__(self):
        self.app_window = Tk()
        self.name = StringVar()
        self.empCheckBox = IntVar()
        self.insCheckBox = IntVar()
        self.stuCheckBox = IntVar()
        self.checkBox = [{"label1": "Employee", "bindVar": self.empCheckBox },
                         {"label1": "Instructor", "bindVar": self.insCheckBox },
                         {"label1": "Student", "bindVar": self.stuCheckBox }]
        self.my_listbox = Listbox()
        self.listBoxVars = ["AK", "AL", "AR", "AZ", "CA", "CO"]
        self.radioButtonVal = StringVar()
        self.radioButtonItems = ["red", "blue", "green"]
        self.setupInterface()

    def drawChecKBoxes(self):
        col_count = 0
        for checkbox1 in self.checkBox:
            Checkbutton(self.app_window, text=checkbox1["label1"],variable=checkbox1['bindVar']).grid(row=1, column=col_count, sticky=NSEW)
            col_count = col_count + 1
    def drawListBox(self):
        scrollBar = Scrollbar(self.app_window, orient=VERTICAL)
        scrollBar.grid(row=2, column=2, sticky=N+S+W)

        self.my_listbox = Listbox(self.app_window, relief = SUNKEN, yscrollcommand=scrollBar.set, selectmode=MULTIPLE)
        self.my_listbox.grid(row=1, column=0, sticky=NSEW)
        list_index = 0
        for listItem in self.listBoxVars:
            self.my_listbox.insert(list_index, listItem)
            list_index = list_index + 1
        scrollBar.config(command=self.my_listbox.yview)

         
    def drawRadioButtons(self):
        col_count = 0
        for radioButton in self.radioButtonItems:
            Radiobutton(self.app_window, text=radioButton, variable=self.radioButtonVal, value=radioButton).grid(row=3, column=col_count, sticky=NSEW)
            col_count = col_count + 1

    def setupGrid(self):
        text_label = TextLabel(self.app_window, "Name", 0, 0)
        text_label.bind("<Button-1>", self.submitData)

        nameField = Entry(self.app_window)
        nameField.grid(row=0, column=1, sticky=NSEW)
        nameField.config(textvariable=self.name)
        nameField.bind("<Return>", self.submitData)

        self.drawChecKBoxes()
        self.drawListBox()
        self.drawRadioButtons()

        submitButton = Button(self.app_window, text="Submit Button")
        submitButton.grid(row=3, column=0, columnspan=2, sticky=NSEW)
        submitButton.bind("<Button-1>", self.submitData)
    
    def setupInterface(self):
        self.app_window.title("GUI App")
        self.setupGrid()
        self.app_window.mainloop()
    
    def submitData(self, *passed_args):
        selecteditems = self.my_listbox.curselection()
        states = " "
        for stateindex in selecteditems:
            states = states + " " + self.listBoxVars[stateindex]
        roles = " "
        if self.empCheckBox.get() == 1:
            roles = roles + "Employee"
        if self.insCheckBox.get() == 1:
            roles = roles + "Instructor"
        if self.stuCheckBox.get() == 1:
            roles = roles + "Student"
        
        print( self.name.get()+ "**" + roles + "has a favorite color of"  + self.radioButtonVal.get() + states)





    