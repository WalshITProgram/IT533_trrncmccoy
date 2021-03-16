from Classes.database_access import *
import pymysql
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
from Classes.database_access import *

class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.book_id = IntVar()
        self.book_store = StringVar()
        self.book_name = StringVar()
        self.book_author = StringVar()
        self.book_isbn = IntVar()
        self.book_copies = IntVar()
        self.book_checked = IntVar()
        self.setupInterface()
    
    def setupGrid(self):
        book_id = Entry(self.root, width=30)
        book_id.grid(row=0, column=1)
        book_id.config(textvariable=self.book_id)
        book_store = Entry(self.root, width=30)
        book_store.grid(row=1, column=1)
        book_store.config(textvariable=self.book_store)
       
        book_name = Entry(self.root, width=30)
        book_name.grid(row=2, column=1)
        book_name.config(textvariable=self.book_name)
       
        book_author = Entry(self.root, width=30)
        book_author.grid(row=3, column=1)
        book_author.config(textvariable=self.book_author)
       
        book_isbn = Entry(self.root, width=30)
        book_isbn.grid(row=4, column=1)
        book_isbn.config(textvariable=self.book_isbn)
       
        book_copies = Entry(self.root, width=30)
        book_copies.grid(row=5, column=1)
        book_copies.config(textvariable=self.book_copies)
       
        book_checked = Entry(self.root, width=30)
        book_checked.grid(row=6, column=1)
        book_checked.config(textvariable=self.book_checked)
        
        book_id_label = Label(self.root, text="Book ID")
        book_id_label.grid(row=0, column=0)

        book_store_label = Label(self.root, text="Book Store")
        book_store_label.grid(row=1, column=0)

        book_name_label = Label(self.root, text="Book Name")
        book_name_label.grid(row=2, column=0)

        book_author_label = Label(self.root, text="Author")
        book_author_label.grid(row=3, column=0)

        book_isbn_label = Label(self.root, text="ISBN")
        book_isbn_label.grid(row=4, column=0)

        book_copies_label = Label(self.root, text="Purchased Copies")
        book_copies_label.grid(row=5, column=0)

        book_checkout_label = Label(self.root, text="Copies Not Checked Out")
        book_checkout_label.grid(row=6, column=0)

        submit_btn = Button(self.root, text="Add Book to Database")
        submit_btn.grid(row=7, column=0)
        submit_btn.bind("<Button-1>", self.submit())

        query_btn = Button(self.root, text="Show Records")
        query_btn.grid(row=7, column=1)
        query_btn.bind("<Button-2>", self.query1())


    def query1(self):
        my_db = DB_Connect('root', '', 'Python_Books', 3307)
        my_result = my_db.executeSelectQuery("SELECT * FROM Book_Table")
        for record in my_result:
            print(str(record))
            break
        

    def submit(self):
        my_db = DB_Connect('root', '', 'Python_Books', 3307)
        my_result = my_db.executeSelectQuery("INSERT INTO Book_Table VALUES (:book_id, :book_store, :book_name, :book_author, :book_isbn, :book_copies, :book_checked)",
                                            {
                                                'book_id': self.book_id.get(),
                                                'book_store': self.book_store.get(),
                                                'book_name': self.book_name.get(),
                                                'book_author': self.book_author.get(),
                                                'book_isbn': self.book_isbn.get(),
                                                'book_copies': self.book_copies.get(),
                                                'book_checked': self.book_checked.get()
                                            }
        )
        # Create Text Box Labels

    def setupInterface(self, *passed_args):
        self.root.title("Book Store")
        self.submit()
        self.query1()
        self.setupGrid()
        self.root.mainloop()