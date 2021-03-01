import sys
from sys import exit
from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *
from tkinter import *
import time 
from threading import *

# importing all files  from tkinter 
from tkinter import * 
from tkinter import ttk 
  
# import only asksaveasfile from filedialog 
# which is used to save file in any extension 
from tkinter.filedialog import asksaveasfile 
class GUI_App():

    def __init__(self):
        """This is a constructor to create variables to use in the class' methods, to create an instance of Tk and to
        call the method that sets up the app's interface"""
        # Create an instance of Tk to build an app window
        self.hw_app_window = Tk()
        # Set size of app window
        self.hw_app_window.geometry("395x307")
        # Create variables to store icon images for submit button
        self.saveIconImage = PhotoImage(file="image_files/saveSettings.png")
        self.loadIconImage = PhotoImage(file="image_files/loadSettings.png")
        # Introduce variables to hold user input from TextEntryBox and NumEntryBox
        self.logFileLocation = StringVar()
        self.serverPort = IntVar()
        # Introduce menu contents of Comboboxes
        self.max_thread_options = [1,2,4]
        self.on_off_options = ["off", "on"]
        # Declare lists of values to use to populate Listboxes with choices
        self.listBoxEventVars = ["application", "security", "error", "input/output"]
        self.listBoxFileTypeVars = [".doc", ".docx", ".ppt", ".pptx", ".xls", ".xlsx",
                                    ".rtf", ".pdf", ".txt", ".jpg", ".png", ".gif",
                                    ".xml", ".html", ".zip", ".mp4", ".mov"]
        # Call the method that builds the app window
        self.setupInterface()


    def getFile(self, *args):
        """This is a method to open a .json file and translate the contents of the file (stored as a 
        Python dictionary) into action to populate text boxes, listboxes, and comboboxes on the app's GUI.
        It can be used as a menu callback handler and/or a button clicked to open a file and get its contents.
        
        Arguments:
            self
            *args -- tuple of additional information 
        
        Returns:
            Nothing. This method runs and populates saved selections on a GUI.
        """
        openFile = askopenfilename()
        # If user selects a file and openFile now has a value, open that file and set contents to a var
        if openFile:
            with open(openFile) as my_file:                
                # Turn contents of file into a python object
                dict_to_open = json.load(my_file)

        # Use .set to populate the GUI with whatever is saved in the dictionary at a given key
        self.max_threads.set(dict_to_open["max_threads"])
        self.logFileLocation.set(dict_to_open["file_location"])
        self.debug_status.set(dict_to_open["debug_status"])
        self.serverPort.set(dict_to_open["server_port_used"])
        # Use a function to find index positions of items selected in listboxes and highlight those
        highlightListboxItemsByIndex(dict_to_open, "type_event", self.listBoxEventVars, self.type_event)
        highlightListboxItemsByIndex(dict_to_open, "supported_file_types", self.listBoxFileTypeVars, self.supported_file_types)


    def setupGrid(self):
        """This is a method to setup a grid for laying out widgets for different fields in the GUI.
        
        Arguments:
            self 
        
        Returns:
            Nothing. This method simply appends a list.
        """
        # Grid positioning for all widgets/elements in the interface
        text_label1 = TextLabel(self.hw_app_window, "Max Threads:", 0, 0, 1, 2)
        self.max_threads = MyCombobox(self.hw_app_window, self.max_thread_options, 0, 3)
        text_label2 = TextLabel(self.hw_app_window, "Event Log File Location:", 1, 0, 1, 2)
        self.file_location = TextEntryBox(self.hw_app_window,1, 3, 1, 2, NSEW, self.logFileLocation)
        text_label3 = TextLabel(self.hw_app_window, "Types of Events to Log:", 2, 0, 1, 2)
        self.type_event = MyListbox(self.hw_app_window, 2, 4, 2, 3, self.listBoxEventVars)
        text_label4 = TextLabel(self.hw_app_window, "Supported File Types:", 3, 0, 1, 2)
        self.supported_file_types = MyListbox(self.hw_app_window, 3, 4, 3, 3, self.listBoxFileTypeVars)
        text_label5 = TextLabel(self.hw_app_window, "Debug Mode (on/off):", 4, 0, 1, 2)
        self.debug_status = MyCombobox(self.hw_app_window, self.on_off_options, 4, 3)
        text_label6 = TextLabel(self.hw_app_window, "Server Port #:", 5, 0, 1, 2)
        self.server_port_used = NumEntryBox(self.hw_app_window, 5, 3, 1, 2, NSEW, self.serverPort)

        # Create submit button to save the settings a user has selected
        submitButton = MyButton(self.hw_app_window, self.submitData, self.saveIconImage, 3, 6, 1)

        # Create load button to populate the GUI with settings that have already been saved
        loadButton = MyButton(self.hw_app_window, self.getFile, self.loadIconImage, 0, 6, 1)


    def setupMenu(self):
        """This is a method to setup a dropdown menu at the top left of the screen.
        
        Arguments:
            self 
        
        Returns:
            Nothing. This method simply creates a menu with options to load settings or save settings.
        """
        topMenu = Menu(self.hw_app_window)
        self.hw_app_window.config(menu=topMenu)

        # Create an instance of Menu to later be associated with whatever word gets printed in the top menu line
        jfiles = Menu(topMenu)
        # First add_command to menu, give it a label, set what callback it calls under command, and use 
        # accelerator to give keyboard shortcut
        jfiles.add_command(label="Load Settings from JSON", command=self.getFile, accelerator="Ctrl+l")
        jfiles.add_command(label="Save Settings to JSON", command=self.submitData, accelerator="Ctrl+s")
        # Set words that appear on top line of the menu
        topMenu.add_cascade(label="Config Settings", menu=jfiles)
        # Create bindings for keyboard shortcuts
        self.hw_app_window.bind_all("<Control-l>", self.getFile)
        self.hw_app_window.bind_all("<Control-s>", self.submitData)


    def setupInterface(self):
        """This is a method to setup the overall app interface with a title in the top bar, a grid full of
        widgets created in another method, and a menu at the top (also created in another method).
        
        Arguments:
            self 
        
        Returns:
            Nothing. This method simply creates what appears to the user as an app full of widgets with 
            a menu.
        """
        # Build a window and put a title in it
        self.hw_app_window.title("Helpdesk Config Help App")
        # Call the setupGrid method to put nicely organized elements from a grid into app window
        self.setupGrid()
        # Setup menu so options drop down from top of screen
        self.setupMenu()
        # Get the window to "run"
        self.hw_app_window.mainloop()

    
    def submitData(self, *passed_args):
        """This is a method to save the settings a user entered and clicked in the GUI as a python dictionary in
        a .json file.  It can be called from a method that creates a save/submit button and/or a menu option for 
        saving/submitting.  It will show users a popup error if they miss a piece of information or provide
        invalid information.
        
        Arguments:
            self
            passed_args -- tuple of additional data
        
        Returns:
            Nothing. This method simply saves settings user entered when they are acceptable.
        """
        # Create variables to pass to a function that returns a string of selected listbox items the user chose
        # Variables for Supported File Types
        selectedSupportedFileTypes = self.supported_file_types.curselection()
        varsInSupportedFileTypeListBox = self.listBoxFileTypeVars
        # Variables for Types of Events to Log
        selectedTypesOfEvents = self.type_event.curselection()
        varsInTypesOfEvent = self.listBoxEventVars
        
        # Use function to pull out the items users selected in each of the two GUI listboxes and set them to variables
        # that can be used when creating dictionary values
        self.supportedTypes = seeSelectedItemsFromListbox(selectedSupportedFileTypes, varsInSupportedFileTypeListBox)
        self.eventsChosen = seeSelectedItemsFromListbox(selectedTypesOfEvents, varsInTypesOfEvent)


        loc_value = self.logFileLocation.get()
        # Validate input to be sure port is in range and location is a legitimate name (at least 4 characters long)
        # and make sure a user hasn't left and selection options completely blank
        try:
            port_value = self.serverPort.get()
            if port_value >= 50000 and port_value <=50500:

                if len(loc_value) >= 4:

                    if self.eventsChosen != "" and self.supportedTypes != "":

                        json_dict = {"max_threads": self.max_threads.get(), "file_location": loc_value, 
                            "type_event": self.eventsChosen, "supported_file_types": self.supportedTypes, 
                            "debug_status": self.debug_status.get(), "server_port_used": port_value}
                        
                        target_file = asksaveasfilename()
                        with open (target_file, "w") as fileToUpdate:
                            json.dump(json_dict, fileToUpdate)
                        
                        messagebox.showinfo(title="Settings Saved", 
                            message="Your settings have been saved for future configuration purposes")

                    else:
                        #pop up an error
                        messagebox.showerror("Invalid Submission", 
                            "Please select at least one supported file type and at least one type of event to log.")    
                else:
                    #pop up an error
                    messagebox.showerror("Invalid Event Log File Location", 
                        "Please enter a valid location for your event log file")
            else:
                #pop up an error
                messagebox.showerror("Invalid Server Port Number", 
                    "Port value must be between 50000 and 50500 (note: enter digits only)")
        except:
            #pop up an error
            messagebox.showerror("Invalid Input", 
                "Settings cannot be saved until valid selections are made and valid input is provided in all fields")


                       self.file_location = Entry(self.app_screen)
        self.file_location.grid(row=6, column=2, sticky=NSEW)
        self.file_location.config(textvariable=self.serverport)


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
