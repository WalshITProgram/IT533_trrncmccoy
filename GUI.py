import sys
from sys import exit
from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *


def show(entries, popup):
    fetch(entries)
    popup.destroy()
def ask():
    popup = Toplevel()
    ents = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda: show(ents, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window()
root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()





'''
demo = { 
    'Open': askopenfilename,
    'Color': askcolor,
    'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'),
    'Error': lambda:showerror('Error!', "He's dead, Jim"),
    'Input': lambda: askfloat('Entry', 'Enter credit card number')
}

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Basic demos").pack()
        for (key, value) in demos.items():
            Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)

if __name__ == '__main__': Demo().mainloop()


def callback():
    if askyesno('Verify', 'Do you really want to quit?'):
        showwarning('Yes', 'Quit not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')
errmsg = 'Sorry, no spam allowed!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)
mainloop()


root = Tk()
trees = [('The Larch!', 'light blue'), 
         ('The Pine!', 'light green'), 
         ('The Giant Redwood!', 'red')]

for (tree, color) in trees:
    win = Toplevel(root)
    win.title("Sing...")
    win.protocol('WM_DELETE_WINDOW', lambda:None)
    win.iconbitmap('py-blue-trans-out.ico')

    msg = Button(win, text=tree, command=win.destroy)
    msg.pack(expand=YES, fill=BOTH)
    msg.config(padx=10, pady=10, bd=10, relief=RAISED)
    msg.config(bg='black', fg=color, font=('times', 30, 'bold italic'))

    root.title('Lumberjack demo')
    Label(root, text='Main Window', width=30).pack()
    Button(root, text='Quit All', command=root.quit).pack()
    root.mainloop()



win1 = T
win2 = Tk()

Button(win1, text='Spam', command=sys.exit).pack()
Button(win2, text='SPAM', command=sys.exit).pack()

Label(text='Popups').pack()
win1.mainloop()

widget = Button(text='Spam', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='gumby')
widget.config(bd=8, relief=RAISED)
widget.config(bg='dark green', fg='white')
widget.config(font=('helvetica', 20, 'underline italic'))
mainloop()

# config restarts its options at any time
root = Tk()
labelfont = ('times', 20, 'bold')
widget = Label(root, text='Hello Config World')
widget.config(bg='black', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()


class Hello(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 42
        self.make_widgets()
    
    def make_widgets(self):
        widget = Button(self, text='Hello Frame World!', command=self.message)
        widget.pack(side=LEFT)

    def message(self):
        self.data += 1
        print('Hello frame world %s!' % self.data)
if __name__=='__main__': 
    Hello().mainloop()

parent = Frame(None)
parent.pack()
Hello(parent).pack(side=RIGHT)
Button(parent, text='Attach', command=exit).pack(side=LEFT)
parent.mainloop()

# Customize Widgets with classes
class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(command=self.callback, fg='red', bg='black', font=('courier', 12), relief=RAISED, bd=5)
    def callback(self):
        print('Goodbye World!')
        self.quit()

if __name__=='__main__':
    HelloButton(text='spam', command=onSpam).mainloop()
 


def greeting():
    print('Hello stdout world!...')
win = Frame()
win.pack()
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT, anchor=N)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=YES)
win.mainloop()
'''

