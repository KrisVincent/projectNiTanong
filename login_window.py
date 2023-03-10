import sqlite3
from tkinter import *
from tkinter import messagebox

import admin_window
import update_window


class login:

    def __init__(self,root):
      self.root = root

    def get_window(self):
        # Label
        master = Toplevel(self.root)
        master.geometry("400x200")
        master.title("Login Admin")
        login_label = Label(master,
                            text="LOGIN",
                            font=("Arial", 20)).place(x=170, y=20)

        username_label = Label(master,
                               text="Username",
                               font=("Arial", 13)).place(x=50, y=70)

        password_label = Label(master,
                               text="Password",
                               font=("Arial", 13)).place(x=50, y=100)

        # Entry/Textarea

        username = StringVar()
        password = StringVar()

        e1 = Entry(master,
                   width=25,
                   textvariable=username)
        e1.place(x=150, y=70)

        e2 = Entry(master,
                   width=25,
                   show="*",
                   textvariable=password)

        e2.place(x=150, y=100)

        # Entry
        login_button = Button(master,
                              width=10,
                              text="Login",
                              font=("Arial", 10),
                              command=lambda:
                              login())

        login_button.place(x=170, y=130)

        #functions

        def login():
            conn = sqlite3.connect("contact_tracerDB.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * from admin_acc "
                           "WHERE username = ? AND password = ?", (username.get(), password.get()))


            result = cursor.fetchall();



            if len(result) == 0:
                master.attributes('-topmost', True)


                messagebox.showinfo("Info", "User not found!",parent=master)
                master.attributes('-topmost', False)


            else:
                messagebox.showinfo("Info", f"Welcome! {result[0][1]}")
                id = result[0][0]
                master.destroy()
                admin_window.menu(self.root,id).get_window()



