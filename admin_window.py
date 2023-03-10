import sqlite3
from tkinter import *
from tkinter import messagebox

import account_table
import contact_tracing_form
import data_management_window
import registration_form
import update_window


class menu:

    def __init__(self,root,id):
        self.root = root
        self.id = id


    def get_window(self):

        root = Toplevel(self.root)
        root.geometry("250x300")
        root.title("Menu")

        edit_button = Button(root,
                              width=15,
                              text="Edit Account",
                              font=("Arial", 10),
                              command=lambda:
                              update()
                              ).place(x=80, y=50)

        addButton = Button(root,
                           width=15,
                           text="Add Account",
                           font=("Arial", 10),
                           command=lambda:
                           add_account()
                           ).place(x=80, y=90)

        manageButton =  Button(root,
                           width=15,
                           text="Manage Account",
                           font=("Arial", 10),
                           command=lambda:
                           manage_account()
                           ).place(x=80, y=130)
        logoutButton = Button(root,
                              width=15,
                              text="Logout",
                              font=("Arial", 10),
                              command=lambda:
                              logout()
                              ).place(x=80, y=210)

        data_management_button = Button(root,
                              width=15,
                              text="Data Management",
                              font=("Arial", 10),
                              command=lambda:
                              manage()
                              ).place(x=80, y=170)



        def manage():
            root.destroy()
            data_management_window.data(self.root,self.id).get_window()


        def logout():
            msg = messagebox.askquestion("Confirm", "Are you sure?")
            if msg == "yes":

               root.destroy()

            else:
                print("do nothing")



        def manage_account():
            root.destroy()
            account_table.table(self.root,self.id).get_window()


        def add_account():
            root.destroy()
            registration_form.registration_window(self.root,self.id).get_window()

        def update():
            root.destroy()
            update_window.update_admin(self.root,self.id).get_window()



        root.mainloop()