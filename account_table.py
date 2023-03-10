import sqlite3
import tkinter as tk
from tkinter import*
from tkinter import ttk, messagebox

import account_update_table
import admin_window
import update_window


class table:

    def __init__(self,root,id):

        self.root = root
        self.get_id = False
        self.id = id

    def get_window(self):
        mainPage = Toplevel(self.root)
        mainPage.title("Account Management")
        mainPage.geometry("720x620")



        s = ttk.Style()
        s.theme_use('clam')


        # Add a Treeview widget
        tree = ttk.Treeview(mainPage, column=("c1", "c2", "c3","c4","c5","c6","c7"), show='headings', height=10)\


        tree.column("# 1", anchor=CENTER, width=50 , stretch=NO)
        tree.heading("# 1", text="ID")
        tree.column("# 2", anchor=CENTER, width=80 , stretch=NO)
        tree.heading("# 2", text="username")
        tree.column("# 3", anchor=CENTER, width=80 , stretch=NO)
        tree.heading("# 3", text="password")
        tree.column("# 4", anchor=CENTER, width=80 , stretch=NO)
        tree.heading("# 4", text="surname")
        tree.column("# 5", anchor=CENTER, width=80 , stretch=NO)
        tree.heading("# 5", text="FName")
        tree.column("# 6", anchor=CENTER, width=80 , stretch=NO)
        tree.heading("# 6", text="middlename")
        tree.column("# 7", anchor=CENTER, width=50 , stretch=NO)
        tree.heading("# 7", text="gender")





        tree.place(x=0)
        # Insert the data in Treeview widget


        buttonOne = Button(mainPage,
                           text="View All",
                           command=lambda:
                                      view())
        buttonOne.place(x=555, y=20, width=150)

        buttonTwo = Button(mainPage,
                           text="Clear",
                           command=lambda:clear())

        buttonTwo.place(x=555, y=50, width=150)

        buttonThree = Button(mainPage,
                             text="Delete",
                             command=lambda:deleteItem())
        buttonThree.place(x=555, y=80, width=150)

        buttonFour = Button(mainPage,
                            text="Edit Selected ",
                            command = lambda :edit())
        buttonFour.place(x=555, y=110, width=150)

        back_menu_button  = Button(mainPage,
                            text="Go Back ",
                            command = lambda :back())

        back_menu_button.place(x = 555, y = 300, width = 150,height = 150)

        def back():
            mainPage.destroy()
            admin_window.menu(self.root, self.id).get_window()


        def messageboxx(title, text):

            mainPage.attributes('-topmost', True)
            messagebox.showinfo(title, text, parent=mainPage)
            mainPage.attributes('-topmost', False)



        def selectItem(a):
            curItem = tree.focus()
            try:
                result = tree.item((curItem))
                get = result['values']
                self.get_id = get[0]
            except:
                messageboxx("Info","Don't click on empty space")


        tree.bind('<ButtonRelease-1>', selectItem)

        def deleteItem():
            conn = sqlite3.connect("contact_tracerDB.db")
            cursor = conn.cursor()

            if self.id == self.get_id:
                messageboxx("Info","You can't delete your own id there ask another admin")

                return

            if self.get_id == False:
                messageboxx("Info","Error 69420")

                return

            try:
                cursor.execute("DELETE from admin_acc WHERE admin_id = ? ", (self.get_id,))

                conn.commit()

                messageboxx("Info",f"Id:{self.get_id} succesfully deleted")




            except :
                messageboxx("Info","Error 69420")


        def view():
            conn = sqlite3.connect("contact_tracerDB.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * from admin_acc ")

            result = cursor.fetchall()


            for item in tree.get_children():
                tree.delete(item)


            for data in result:
                tree.insert('', 'end', values=data)

        def clear():
            for item in tree.get_children():
                tree.delete(item)

            self.get_id = False

        def edit():
             account_update_table.update_account(self.root,self.get_id).get_window()



        mainPage.mainloop()