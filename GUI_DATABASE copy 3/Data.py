from tkinter import * 
import sqlite3

root = Tk()
root.title('Book Store')
root.geometry("1000x500")

conn = sqlite3.connect('Book.db')
c = conn.cursor()
'''
c.execute("""CREATE TABLE books (
        book_id integer,
        book_name text,
        Author text,
        ISBN integer
        Purchase_Copies integer,
        Copies integer
        Checkout integer
        )""" )

addColumn = "ALTER TABLE books ADD COLUMN Not_Checkedout varchar(32)"

c.execute(addColumn)
'''
def ValidateTitle():
    passed_title = book_name.get()
    print(passed_title)

def Validate_name():
    valid_name_chars = [" ",'\'','-']
    while True:
        Book_name = book_author.get()
        if len(Book_name) == 0:
            continue
        bad_char_hit = False
# Create a for loop to iterate through chars entered 
        for letter in Book_name:
    # Set condition statement to test if the input has letters and valid chars
            if letter not in valid_name_chars and not letter.isalpha():
                bad_char_hit = True
# if returned false add employee name      
        if bad_char_hit == False:
            print(Book_name)
            break

def Validate_ISBN():
    	while True:
            Book_ID = book_isbn.get()
            # If less then 7 and not a int must repeat input
            if (len(Book_ID) <= 9):
                # If valid add it to employee dict [ID]
                try:
                    int(Book_ID)
                    print(Book_ID)
                    break
                except: 
                    print("You entered an invalid ID number! Please try again.")


def Validate_Check_Out():
    passed_Check_Out = book_checked.get()
    try:
        int(passed_Check_Out)
        print(passed_Check_Out)
    except:
        print("Enter Amount of Checked Out Books")

def Validate_Book_Copies():
    passed_book_copies = book_copies.get()
    try:
        int(passed_book_copies)
        print(passed_book_copies)
    except:
        print("Enter Amount of Books Copies")

def update():
    conn = sqlite3.connect('Book.db')

    c = conn.cursor()
    book_record_id = delete_book.get()
    c.execute(""" UPDATE books SET 
        book_id = :book_id,
        book_name = : book_name,
        Author = :book_author, 
        ISBN = :book_isbn,
        Purchase_Copies = :book_copies,
        Not_Checkedout = :book_checked
        WHERE oid = :oid""",
        {
            'book_id': book_id_edit.get(),
            'book_name': book_name_edit.get(),
            'book_author': book_author_edit.get(),
            'book_isbn' : book_isbn_edit.get(),
            'book_copies': book_copies_edit.get(),
            'book_checked': book_checked_edit.get(),
            'oid': book_record_id.get()
        }
        )
    
    editor.destroy()

    conn.commit()

    conn.close()

def edit():
    global editor
    editor = Tk()
    editor.title('Update Book Records')
    editor.geometry("1000x500")
    global book_id_edit
    global book_name_edit
    global book_author_edit
    global book_isbn_edit
    global book_copies_edit
    global book_checked_edit

    book_id_edit = Entry(editor, width=30)
    book_id_edit.grid(row=0, column=1)

    book_name_edit = Entry(editor, width=30)
    book_name_edit.grid(row=2, column=1)

    book_author_edit = Entry(editor, width=30)
    book_author_edit.grid(row=3, column=1)

    book_isbn_edit = Entry(editor, width=30)
    book_isbn_edit.grid(row=4, column=1)


    book_copies_edit = Entry(editor, width=30)
    book_copies_edit.grid(row=5, column=1)

    book_checked_edit = Entry(editor, width=30)
    book_checked_edit.grid(row=6, column=1)


    book_id_label = Label(editor, text="Book ID")
    book_id_label.grid(row=0, column=0)

    book_name_label = Label(editor, text="Book Name")
    book_name_label.grid(row=2, column=0)

    book_author_label = Label(editor, text="Author")
    book_author_label.grid(row=3, column=0)

    book_isbn_label = Label(editor, text="ISBN")
    book_isbn_label.grid(row=4, column=0)

    book_copies_label = Label(editor, text="Purchased Copies")
    book_copies_label.grid(row=5, column=0)

    book_checkout_label = Label(editor, text="Copies Not Checked Out")
    book_checkout_label.grid(row=6, column=0)


    edit_btn = Button(editor, text="Save Book", command=update)
    edit_btn.grid(row=8, column=0)

    conn = sqlite3.connect('Book.db')
    c = conn.cursor()

    book_record_id = delete_book.get()
    c.execute("SELECT * FROM books WHERE oid = " + book_record_id)
    book_records = c.fetchall()
    for books in book_records:
        book_id_edit.insert(0, books[0])
        book_name_edit.insert(0, books[1])
        book_author_edit.insert(0, books[2])
        book_isbn_edit.insert(0, books[3])
        book_copies_edit.insert(0, books[4])
        book_checked_edit.insert(0, books[5])
        


def delete():
    conn = sqlite3.connect('Book.db')

    c = conn.cursor()

    c.execute("DELETE from books WHERE oid = " + delete_book.get())


    conn.commit()

    conn.close()


def submit():
    conn = sqlite3.connect('Book.db')
    c = conn.cursor()
    c.execute("INSERT INTO books Values (:book_id, :book_name, :book_author, :book_isbn, :book_copies, :book_checked)",
            {
                'book_id': book_id.get(),
                'book_name': book_name.get(),
                'book_author': book_author.get(),
                'book_isbn': book_isbn.get(),
                'book_copies': book_copies.get(),
                'book_checked': book_checked.get()

            }
    
    )
    conn.commit()

    conn.close() 

    book_id.delete(0,END)
    book_name.delete(0,END)
    book_author.delete(0,END)
    book_isbn.delete(0,END)
    book_copies.delete(0, END)
    book_checked.delete(0,END)

def query():
    conn = sqlite3.connect('Book.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM books")
    book_records = c.fetchall()
    print(book_records)

    print_book_records = ''
    for book_record in book_records:
        print_book_records += "Book" + " " + "ID:" + str(book_record[0]) + " / " + " Name:" + str(book_record[1]) + " / " + " Author:" + str(book_record[2]) + " / " + " ISBN:" + str(book_record[3]) + " / " + "Purchased Copies:" + str(book_record[4]) + " / " + "Not Checked Out:" + str(book_record[5]) + "\n"
        
    
    query_label = Label(root, text=print_book_records)
    query_label.grid(row=8, column=1)
    
    conn.commit()
    conn.close()


book_id = Entry(root, width=30)
book_id.grid(row=0, column=1)

book_name = Entry(root, width=30)
book_name.grid(row=2, column=1)

book_author = Entry(root, width=30)
book_author.grid(row=3, column=1)

book_isbn = Entry(root, width=30)
book_isbn.grid(row=4, column=1)


book_copies = Entry(root, width=30)
book_copies.grid(row=5, column=1)

book_checked = Entry(root, width=30)
book_checked.grid(row=6, column=1)

delete_book = Entry(root, width=30)
delete_book.grid(row=7, column=1)

book_id_label = Label(root, text="Book ID")
book_id_label.grid(row=0, column=0)

book_name_label = Label(root, text="Book Name")
book_name_label.grid(row=2, column=0)

book_author_label = Label(root, text="Author")
book_author_label.grid(row=3, column=0)

book_isbn_label = Label(root, text="ISBN")
book_isbn_label.grid(row=4, column=0)

book_copies_label = Label(root, text="Purchased Copies")
book_copies_label.grid(row=5, column=0)

book_checkout_label = Label(root, text="Copies Not Checked Out")
book_checkout_label.grid(row=6, column=0)

delete_book_label = Label(root, text="Delete Book ID Number")
delete_book_label.grid(row=7, column=0)

submit_btn = Button(root, text="Add Book", command=submit)
submit_btn.grid(row=8, column=0)

query_btn = Button(root, text="Show Books", command=query)
query_btn.grid(row=9, column=0)

delete_btn = Button(root, text="Delete Book", command=delete)
delete_btn.grid(row=11, column=0)

edit_btn = Button(root, text="Edit Book", command=edit)
edit_btn.grid(row=12, column=0)

conn.commit()
conn.close()

root.mainloop()