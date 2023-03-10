from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox




# class EntryWithPlaceholder(tk.Entry):
#     def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
#         super().__init__(master)
#
#         self.placeholder = placeholder
#         self.placeholder_color = color
#         self.default_fg_color = self['fg']
#
#         self.bind("<FocusIn>", self.foc_in)
#         self.bind("<FocusOut>", self.foc_out)
#
#         self.put_placeholder()
#
#     def put_placeholder(self):
#         self.insert(0, self.placeholder)
#         self['fg'] = self.placeholder_color
#
#     def foc_in(self, *args):
#         if self['fg'] == self.placeholder_color:
#             self.delete('0', 'end')
#             self['fg'] = self.default_fg_color
#
#     def foc_out(self, *args):
#         if not self.get():
#             self.put_placeholder()
import admin_window


class registration_window:
    def __init__(self,root,id):
        self.root = root
        self.id = id


    def get_window(self):
        root = Toplevel(self.root)
        root.geometry("400x500")
        root.title("Add Account")
        get_username = StringVar()
        get_password = StringVar()
        get_confirm = StringVar()
        get_surname = StringVar()
        get_firstname = StringVar()
        get_middlename = StringVar()
        get_gender = StringVar()

        username = Entry(root, textvariable=get_username, width=25)
        username.pack()

        username.place(x=105, y=25)

        user_label = Label(root, text="Username")
        user_label.pack()
        user_label.place(x=35, y=25)

        userpass = Entry(root, textvariable=get_password, width=25, show="*")
        userpass.pack()
        userpass.place(x=105, y=75)

        pass_label = Label(root, text="Password")
        pass_label.pack()
        pass_label.place(x=35, y=75)

        confirmpass = Entry(root, width=25, textvariable=get_confirm, show="*", )
        confirmpass.pack()
        confirmpass.place(x=105, y=125)

        confirm_label = Label(root, text="Confirm Password")
        confirm_label.pack()
        confirm_label.place(x=1, y=125)

        surname = Entry(root, textvariable=get_surname, width=25)
        surname.pack()
        surname.place(x=105, y=175)

        surname_label = Label(root, text="Surname")
        surname_label.pack()
        surname_label.place(x=35, y=175)

        firstname = Entry(root, textvariable=get_firstname, width=25)
        firstname.pack()
        firstname.place(x=105, y=225)

        firstname_label = Label(root, text="First Name")
        firstname_label.pack()
        firstname_label.place(x=25, y=225)

        middlename = Entry(root, textvariable=get_middlename, width=25)
        middlename.pack()
        middlename.place(x=105, y=275)

        middlename_label = Label(root, text="Middle Name")
        middlename_label.pack()
        middlename_label.place(x=15, y=275)

        genderLabel = Label(root, text="Gender")
        genderLabel.pack()
        genderLabel.place(x=35, y=315)

        maleRB = Radiobutton(root, text="Male", variable=get_gender, value="male")
        maleRB.pack()
        maleRB.place(x=100, y=315)

        femaleRB = Radiobutton(root, text="Female", variable=get_gender, value="female")
        femaleRB.pack()
        femaleRB.place(x=170, y=315)



        back_menu_button  = Button(root,
                            text="Go Back ",
                            command = lambda:back())

        back_menu_button.place(x =105, y = 400, width = 50,height = 50)

        def back():
            root.destroy()
            admin_window.menu(self.root,self.id).get_window()


        def buttonclick():
            msg = messagebox.askquestion("Confirm", "Are you sure?")

            conn = sqlite3.connect("contact_tracerDB.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * from admin_acc "
                           "WHERE username = ? ", [get_username.get()])
            result = cursor.fetchall()
            print(result,get_password.get()==get_confirm.get())
            conn.close()
            if len(result) == 0 and (get_password.get() == get_confirm.get()):

                if msg == "yes":

                    try:
                        conn = sqlite3.connect("contact_tracerDB.db")
                        cursor = conn.cursor()

                        cursor.execute("INSERT INTO admin_acc("
                                       "username,password,surname,firstname,middlename,gender)"
                                       "VALUES (? ,? ,?, ?, ?, ?)",
                                       (get_username.get(), get_password.get(), surname.get(), get_firstname.get(),
                                        get_middlename.get(), get_gender.get()))
                        conn.commit()
                        messagebox.showinfo("Info", "Successfully Registered!")
                    except:
                        messagebox.showinfo("Info", "Error 404")

            elif get_password.get() != get_confirm.get():
                messagebox.showinfo("Info", "Password don't match")
            else:
                print(get_username.get())
                messagebox.showinfo("Info", f"Username {result[0][1]} already taken")

        submitButton = Button(root, text="Submit", command=lambda: buttonclick())
        submitButton.pack()
        submitButton.place(x=105, y=340)

        root.mainloop()
