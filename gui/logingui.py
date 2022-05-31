from tkinter import *


class LoginFrame(Frame):
    def __init__(self, container, notebook):
        super().__init__(container)
        self.notebook = notebook
        self.Heading1 = Label(self, text="LOGIN SYSTEM")
        self.Heading1.grid(row=2, column=1, padx=9, pady=9)
        self.Heading1 = Label(self, text="ENTER USERNAME")
        self.Heading1.grid(row=3, column=0, padx=9, pady=9)
        self.id = Entry(self)
        self.id.grid(row=3, column=1)
        self.Lable_text = Label(self, text="ENTER PASSWORD")
        self.Lable_text.grid(row=5, column=0, padx=9, pady=9)
        self.password = Entry(self)
        self.password.grid(row=5, column=1)
        Heading3 = Button(self, text='Submit', width=22, bg='blue', fg='grey', command=self.Login_method)
        Heading3.grid(row=7, column=1)

    def Login_method(self):

        if self.id.get() == 'manager' and self.password.get() == '123':
            self.notebook.tab(1, state="normal")
            self.notebook.tab(2, state="normal")

        elif self.id.get() == 'coordinator' and self.password.get() == '123':
            self.notebook.tab(2, state="normal")

        else:
            return
