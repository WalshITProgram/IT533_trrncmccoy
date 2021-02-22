from tkinter import *
import logging
import threading
import time
import concurrent.futures
        self.make_widgets('options')
        self.selection = StringVar()
        self.app_screen.geometry("700x450") 
        self.setupGrid()


        self.setupInterface()

    
    def setupGrid(self):
        log = TextFont(self.app_screen, "Log Location", 1, 1)
        log.bind("<Button-1>", self.submitData)
        event = TextFont(self.app_screen, "Log Events", 2, 1)
        event.bind("<Button-1>", self.submitData)
        file_type = TextFont(self.app_screen, "File Type", 3, 1)
        file_type.bind("<Button-1>", self.submitData)
        debug = TextFont(self.app_screen, "Debug Mode", 4, 1)
        debug.bind("<Button-1>", self.submitData)
        server = TextFont(self.app_screen, "Server Port",5, 1)
        server.bind("<Button-1>", self.submitData)

        Field = Entry(self.app_screen)
        Field.grid(row=6, column=1, sticky=NSEW)
        Field.config(textvariable=self.selection)
        Field.bind("<Return>", self.submitData)

        submit = Button(self.app_screen, text="Submit")
        submit.grid(row=6, column=2, sticky=NSEW)
        submit.bind("<Button-1>", self.submitData)

    
    def setupInterface(self):
        self.app_screen.title("Help Desk Menu")
        self.setupGrid()
        self.app_screen.mainloop()
    
    def submitData(self, *passed_args):
        itemselection = self.file_listbox.curselection()
        files = " "
        for file_index in itemselection:
            files = files + " " + self.listBoxVars[file_index]
        print(self.selection.get() + files)
def thread_function(file_location, file_type):
    logging.info(file_location)
    time.sleep(2)
    logging.info(file_type)


if __name__=="__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    threads = list()
    for index in range(3):
        logging.info("Main : before joining thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        logging.info("Main : before joining thread %d.", index)
        thread.join()
        logging.info("Main : thread %d done", index)

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executer:
        executer.map(thread_function, range(3))

             self.my_textbox.delete("1.0", END)
                self.my_textbox.insert("1.0", file_contents)
                self.my_textbox.mark_set(INSERT, "1.0")
                self.my_textbox.focus()

'''


class My_app():
    def __init__(self):
        self.app_screen = Tk()
        self.setupInterface()

    def configapp(self, *args):
        print('Configuration')
    
    def thread(self, *args):
        print('Threads')

    def event_location(self, *args):
        print('Log File Location')

    def eventtypes(self, *args):
        print('Event Type')

    def filetype(self, *args):
        print('File Type')

    def serverport(self, *args):
        print("Server Port")

    def setupMenu(self):
        topMenu = Menu(self.app_screen)
        self.app_screen.config(menu=topMenu)
        Main = Menu(topMenu)
        Main.add_command(label="Thread Selection", command=self.thread)
        Main.add_command(label="Log File Location", command=self.event_location)
        Main.add_command(label="Event Type", command=self.event_location)
        Main.add_command(label="File Type", command=self.eventtypes)
        Main.add_command(label="Server Port", command=self.serverport)
        topMenu.add_cascade(label="Options", menu=Main)

    def setupInterface():
        self.app_screen.title('Menu')
        self.setupMenu
        self.app_screen.mainloop()

if __name__=='__main__': 
    My_app()



    def __init__(self):
        self.app_screen = Tk()
        self.selection = StringVar()
        self.file_listbox = Listbox()
        self.listBoxVars = [".doc", "docx", ".ppt" ".pptx", " .xls", ".xslx", 
                            ".rtf", ".pdf", ".txt", ".jpg", ".png", ".gif", 
                            ".xml", ".html", ".zip", ".mp4", ".mov" ]

        self.setupInterface()

    def drawListbox(self):
        scroll = Scrollbar(self.app_screen, orient=VERTICAL)
        scroll.grid(row=1, column=4, sticky=N+S+W)

        self.file_listbox = Listbox(self.app_screen, relief=SUNKEN, yscrollcommand=scroll.set, selectmode=MULTIPLE)
        self.file_listbox.grid(row=1,column=3, rowspan=8, sticky=NSEW)
        file_list_index = 0
        for listItem in self.listBoxVars:
            self.file_listbox.insert(file_list_index, listItem)
            file_list_index = file_list_index + 1

        scroll.config(command=self.file_listbox.yview) 

    def setupGrid(self):
        log = TextFont(self.app_screen, "Log Location", 1, 1)
        log.bind("<Button-1>", self.submitData)
        event = TextFont(self.app_screen, "Log Events", 2, 1)
        event.bind("<Button-1>", self.submitData)
        file_type = TextFont(self.app_screen, "File Type", 3, 1)
        file_type.bind("<Button-1>", self.submitData)
        debug = TextFont(self.app_screen, "Debug Mode", 4, 1)
        debug.bind("<Button-1>", self.submitData)
        server = TextFont(self.app_screen, "Server Port",5, 1)
        server.bind("<Button-1>", self.submitData)

        Field = Entry(self.app_screen)
        Field.grid(row=6, column=1, sticky=NSEW)
        Field.config(textvariable=self.selection)
        Field.bind("<Return>", self.submitData)

        submit = Button(self.app_screen, text="Submit")
        submit.grid(row=6, column=2, sticky=NSEW)
        submit.bind("<Button-1>", self.submitData)
    
    def setupInterface(self):
        self.app_screen.title("Help Desk Menu")
        self.setupGrid()
        self.drawListbox()
        self.app_screen.mainloop()
    
    def submitData(self, *passed_args):
        itemselection = self.file_listbox.curselection()
        files = " "
        for file_index in itemselection:
            files = files + " " + self.listBoxVars[file_index]
        print(self.selection.get() + files)

            def settext(self, text='', file=None):
        if file: 
            text= open(file, 'r').read()
            self.text.delete('1.0', END)
            self.text.insert('1.0', text)

            self.text.mark_set(INSERT, '1.0')
            self.text.focus()
    def gettext(self):
        return self.text.get('1.0', END+'-1c')


'''