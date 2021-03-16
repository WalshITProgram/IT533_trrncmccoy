from tkinter import *

class Text(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.make_widgets()
        self.settext(text, file)

    def make_widgets(self):
        sbar = Scrollbar(self)
        List = Listbox(self, relief=SUNKEN)
        sbar.config(command=List.yview)
        List.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        List.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text

    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.text.delete('1.0', END)
        self.text.insert('1.0', text)
        self.text.mark_set(INSERT, '1.0')
        self.text.focus()
    def gettext(self):
        return self.text.get('1.0', END+'-1c')


if __name__=='__main__':
    root = Tk()
    if len(sys.argv) > 1:
        st = Text(file=sys.argv[1])
    else:
        st = Text(text='Words\ngo here')
    def show(event):
        print(repr(st.gettext()))
    root.bind('<Key-Escape>', show)
    root.mainloop()
        