import sqlite3
from tkinter import *
from tkinter import messagebox

import admin_window


class update_account:

    def __init__(self,root,id):
        self.id = id
        self.root = root

        conn = sqlite3.connect("contact_tracerDB.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * from admin_acc "
                       "WHERE admin_id = ? ", (self.id,))

        result = cursor.fetchall();

        self.result = result


    def get_window(self):
        root = Toplevel(self.root)
        root.geometry("400x500")

        get_username = StringVar()
        get_password = StringVar()
        get_confirm = StringVar()
        get_surname = StringVar()
        get_firstname = StringVar()
        get_middlename = StringVar()
        get_gender = StringVar()

        username = Entry(root, textvariable=get_username, width=25)
        username.insert(0, self.result[0][1])
        username.config(state=DISABLED)
        username.pack()

        username.place(x=105, y=25)

        user_label = Label(root, text="Username")
        user_label.pack()
        user_label.place(x=35, y=25)

        userpass = Entry(root, textvariable=get_password, width=25, show="*")
        userpass.insert(0, self.result[0][2])
        userpass.pack()
        userpass.place(x=105, y=75)

        pass_label = Label(root, text="Password")
        pass_label.pack()
        pass_label.place(x=35, y=75)

        confirmpass = Entry(root, width=25, textvariable=get_confirm, show="*", )
        confirmpass.insert(0, self.result[0][2])
        confirmpass.pack()
        confirmpass.place(x=105, y=125)

        confirm_label = Label(root, text="Confirm Password")
        confirm_label.pack()
        confirm_label.place(x=1, y=125)

        surname = Entry(root, textvariable=get_surname, width=25)
        surname.insert(0, self.result[0][3])
        surname.pack()
        surname.place(x=105, y=175)

        surname_label = Label(root, text="Surname")
        surname_label.pack()
        surname_label.place(x=35, y=175)

        firstname = Entry(root, textvariable=get_firstname, width=25)
        firstname.insert(0, self.result[0][4])
        firstname.pack()
        firstname.place(x=105, y=225)

        firstname_label = Label(root, text="First Name")
        firstname_label.pack()
        firstname_label.place(x=25, y=225)

        middlename = Entry(root, textvariable=get_middlename, width=25)
        middlename.insert(0, self.result[0][5])
        middlename.pack()
        middlename.place(x=105, y=275)

        middlename_label = Label(root, text="Middle Name")
        middlename_label.pack()
        middlename_label.place(x=15, y=275)

        genderLabel = Label(root, text="Gender")
        genderLabel.pack()
        genderLabel.place(x=35, y=315)

        maleRB = Radiobutton(root, text="Male", variable=get_gender, value="Male")
        maleRB.pack()
        maleRB.place(x=100, y=315)

        femaleRB = Radiobutton(root, text="Female", variable=get_gender, value="Female")
        femaleRB.pack()
        femaleRB.place(x=170, y=315)

        updateButton = Button(root,
                             width=10,
                             text="Update",
                             font=("Arial", 10),
                             command=lambda:
                             update_account()
                             ).place(x=100, y=360)




        def messageboxx(title, text):

            root.attributes('-topmost', True)
            messagebox.showinfo(title, text, parent=root)
            root.attributes('-topmost', False)


        def update_account():
            conn = sqlite3.connect("contact_tracerDB.db")
            cursor = conn.cursor()

            msg = messagebox.askquestion("Confirm", "Are you sure?")

            if get_password.get() == get_confirm.get() and msg == "yes":

                try:
                    cursor.execute(
                        'UPDATE admin_acc '
                        'SET password=?,surname = ?, firstname = ?, middlename = ?,gender = ?'
                        ' WHERE admin_id=?',
                        (get_password.get(),get_surname.get(),get_firstname.get(),get_middlename.get(),get_gender.get(),
                         self.id)
                         )
                    conn.commit()


                except Exception as e:
                    print(e)


            elif get_password.get() != get_confirm.get():
                messageboxx("Info", "Password don't match")
            else:
                messageboxx("Info", "Error 4040")



