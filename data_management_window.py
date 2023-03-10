import base64
import sqlite3
import tkinter as tk
from tkinter import*
from tkinter import ttk, messagebox

from PIL import ImageTk

from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

import io
from tkinter import ttk


import admin_window
import update_window

class data:

    def __init__(self,root,id):
        self.root = root
        self.id = id
        self.selected = False

    def get_window(self):
        root = Toplevel(self.root)
        root.title("Respondents Data Management")
        root.geometry("1120x650")


        tree = ttk.Treeview(root, column=("c1","c2", "c3","c4",
                                          "c5","c6","c7","c8","c9","c10"), show='headings', height=6)\

        s = ttk.Style()
        s.theme_use('clam')

        tree.column("# 1", anchor=CENTER, width=40 , stretch=NO)
        tree.heading("# 1", text="ID")
        tree.column("# 2", anchor=CENTER, width=120 , stretch=NO)
        tree.heading("# 2", text="Surname")
        tree.column("# 3", anchor=CENTER, width=120 , stretch=NO)
        tree.heading("# 3", text="First Name")
        tree.column("# 4", anchor=CENTER, width=50 , stretch=NO)
        tree.heading("# 4", text="M.I.")
        tree.column("# 5", anchor=CENTER, width=80 , stretch=NO)
        tree.heading("# 5", text="Gender")
        tree.column("# 6", anchor=CENTER, width=80 , stretch=NO)
        tree.heading("# 6", text="Temperature")
        tree.column("# 7", anchor=CENTER, width=200 , stretch=NO)
        tree.heading("# 7", text="Address")
        tree.column("# 8", anchor=CENTER, width=120, stretch=NO)
        tree.heading("# 8", text="Email")
        tree.column("# 9", anchor=CENTER, width=120, stretch=NO)
        tree.heading("# 9", text="Number")
        tree.column("# 10", anchor=CENTER, width=120, stretch=NO)
        tree.heading("# 10", text="Birthday")


        tree.place(x=0)

        vsb = Scrollbar(root, orient="vertical", command=tree.yview)
        vsb.place(x=1055,relheight=0.25,)
        tree.configure(yscrollcommand=vsb.set)

        buttonOne = Button(root,
                           text="View All",
                           command=lambda:
                                      view())
        buttonOne.place(x=25, y=200, width=150)

        buttonTwo = Button(root,
                           text="Clear",
                           command=lambda:
                                      clear())
        buttonTwo.place(x=25, y=230, width=150)

        buttonThree = Button(root,
                           text="Delete",
                           command=lambda:
                           deleteItem())
        buttonThree.place(x=25, y=260, width=150)



        back_menu_button = Button(root,
                                  text="Go Back ",
                                  command=lambda: back())

        back_menu_button.place(x=105, y=400, width=50, height=50)

        picture_label = Label(root,
                              text="Picture Shown Below")
        picture_label.place(x=700, y=180)

        THone = Label(root, text="1. Did you travel to Metro Manila within 14 days?")
        THone.pack()
        THone.place(x=200, y=190)

        thoneYES = Entry(root)
        thoneYES.config(state=DISABLED)
        thoneYES.pack()

        thoneYES.place(x=225, y=210)



        THtwo = Label(root, text="2. Did you visit other country one month before coming to this facility?")
        THtwo.pack()
        THtwo.place(x=200, y=250)

        thtwoYES = Entry(root)
        thtwoYES.pack()
        thtwoYES.config(state=DISABLED)
        thtwoYES.place(x=225, y=280)


        THthree = Label(root, text="3. Did you encounter someone who is porbable , suspected and positive")
        THthree.pack()
        THthree.place(x=200, y=310)

        ththree = Label(root, text=" case within 14 days?")
        ththree.pack()
        ththree.place(x=200, y=325)

        ththreeYES = Entry(root)
        ththreeYES.pack()
        ththreeYES.config(state=DISABLED)
        ththreeYES.place(x=225, y=355)

        symptompsLabel = Label(root, text="SYMPTOMS")
        symptompsLabel.pack()
        symptompsLabel.place(x=225, y=400)

        fstsymptom = Label(root, text="-Fever")
        fstsymptom.pack()

        fstsymptom.place(x=225, y=420)

        fsts = Entry(root,width = 8)
        fsts.pack()
        fsts.config(state=DISABLED)
        fsts.place(x=310,y = 420)

        scndsymptom = Label(root, text="-Sore Throat")
        scndsymptom.pack()
        scndsymptom.place(x=225, y=440)

        scnds = Entry(root, width=8)
        scnds.pack()
        scnds.config(state=DISABLED)
        scnds.place(x=310, y=440)

        trdsymptom = Label(root, text="-Cough")
        trdsymptom.pack()
        trdsymptom.place(x=225, y=460)

        trds = Entry(root, width=8)
        trds.pack()
        trds.config(state=DISABLED)
        trds.place(x=310, y=460)

        frtsymptom = Label(root, text="-Cold")
        frtsymptom.pack()
        frtsymptom.place(x=225, y=480)

        frts = Entry(root, width=8)
        frts.pack()
        frts.config(state=DISABLED)
        frts.place(x=310, y=480)

        fifsymptom = Label(root, text="-Chills")
        fifsymptom.pack()
        fifsymptom.place(x=225, y=500)

        fif = Entry(root, width=8)
        fif.pack()
        fif.config(state=DISABLED)
        fif.place(x=310, y=500)

        sixsymptom = Label(root, text="-Skin Rashes")
        sixsymptom.pack()

        sixsymptom.place(x=450, y=420)

        six = Entry(root, width=8)
        six.config(state=DISABLED)
        six.pack()
        six.place(x=580, y=420)

        sevsymptom = Label(root, text="-Body Pain")
        sevsymptom.pack()
        sevsymptom.place(x=450, y=440)

        sev = Entry(root, width=8)
        sev.pack()
        sev.config(state=DISABLED)
        sev.place(x=580, y=440)

        eitsymptom = Label(root, text="-Loss of Appetite ")
        eitsymptom.pack()
        eitsymptom.place(x=450, y=460)

        eits = Entry(root, width=8)
        eits.pack()
        eits.config(state=DISABLED)
        eits.place(x=580, y=460)

        ninsymptom = Label(root, text="-Loss of Smell")
        ninsymptom.pack()
        ninsymptom.place(x=450, y=480)

        nin = Entry(root, width=8)
        nin.pack()
        nin.config(state=DISABLED)
        nin.place(x=580, y=480)

        tensymptom = Label(root, text="-Loss of Taste")
        tensymptom.pack()
        tensymptom.place(x=450, y=500)

        ten = Entry(root, width=8)
        ten.pack()
        ten.config(state=DISABLED)
        ten.place(x=580, y=500)

        def back():
            root.destroy()
            admin_window.menu(self.root, self.id).get_window()

        def deleteItem():
            conn = sqlite3.connect("contact_tracerDB.db")
            cursor = conn.cursor()



            try:
                cursor.execute("DELETE from respondents_data WHERE respond_id = ? ", (self.selected,))

                conn.commit()

                messageboxx("Info","Successfully Deleted")
            except:
                messageboxx("Info","Errorr")



        def messageboxx(title, text):
            root.attributes('-topmost', True)
            messagebox.showinfo(title, text, parent=root)
            root.attributes('-topmost', False)

        def view():
            conn = sqlite3.connect("contact_tracerDB.db")
            cursor = conn.cursor()

            cursor.execute("SELECT respond_id,surname,firstname,MI,gender,temperature,"
                           "address,email,number,birthday from respondents_data ")

            result = cursor.fetchall()

            for item in tree.get_children():
                tree.delete(item)

            for data in result:
                tree.insert('', 'end', values=data)





        def selectItem(a):
            curItem = tree.focus()
            try:

                result = tree.item((curItem))
                get = result['values']
                self.selected = get[0]
                conn = sqlite3.connect("contact_tracerDB.db")
                cursor = conn.cursor()

                cursor.execute("SELECT user_picture from respondents_data "
                               "WHERE respond_id = ?", (self.selected,))

                img = cursor.fetchall()

                img = ImageTk.PhotoImage(Image.open(io.BytesIO(img[0][0])))
                label1 = Label(root, image = img)
                label1.image = img

                label1.place(x=700,y= 210)

                cursor.execute("SELECT * from respondents_travel_history "
                               "WHERE respond_id = ?", (self.selected,))

                result = cursor.fetchall()

                q1 = result[0][1]
                q2 = result[0][2]
                q3 = result[0][3]



                thoneYES.config(state="normal")
                thoneYES.delete(0,"end")
                thoneYES.insert(0,"Yes" if q1 == 1 else "No")
                thoneYES.config(state=DISABLED)

                thtwoYES.config(state="normal")
                thtwoYES.delete(0, "end")
                thtwoYES.insert(0, "Yes" if q2 == 1 else "No")
                thtwoYES.config(state=DISABLED)

                ththreeYES.config(state="normal")
                ththreeYES.delete(0, "end")
                ththreeYES.insert(0, "Yes" if q3 == 1 else "No")
                ththreeYES.config(state=DISABLED)

                cursor.execute("SELECT * from respondents_syndrome "
                               "WHERE respond_id = ?", (self.selected,))

                result = cursor.fetchall()

                symp1 = result[0][1]
                symp2 = result[0][2]
                symp3 = result[0][3]
                symp4 = result[0][4]
                symp5 = result[0][5]
                symp6 = result[0][6]
                symp7 = result[0][7]
                symp8 = result[0][8]
                symp9 = result[0][9]
                symp10 = result[0][10]

                print(symp1)
                fsts.config(state="normal")
                fsts.delete(0,"end")
                fsts.insert(0,"Yes" if symp1 == "True" else "No")
                fsts.config(state=DISABLED)

                scnds.config(state="normal")
                scnds.delete(0,"end")
                scnds.insert(0,"Yes" if symp2 == "True" else "No")
                scnds.config(state=DISABLED)

                trds.config(state="normal")
                trds.delete(0,"end")
                trds.insert(0,"Yes" if symp3 == "True" else "No")
                trds.config(state=DISABLED)

                frts.config(state="normal")
                frts.delete(0,"end")
                frts.insert(0,"Yes" if symp4 == "True"  else "No")
                frts.config(state=DISABLED)


                fif.config(state="normal")
                fif.delete(0,"end")
                fif.insert(0,"Yes" if symp5 == "True"  else "No")
                fif.config(state=DISABLED)

                six.config(state="normal")
                six.delete(0,"end")
                six.insert(0,"Yes" if symp6 == "True" else "No")
                six.config(state=DISABLED)

                sev.config(state="normal")
                sev.delete(0,"end")
                sev.insert(0,"Yes" if symp7 == "True" else "No")
                sev.config(state=DISABLED)

                eits.config(state="normal")
                eits.delete(0,"end")
                eits.insert(0,"Yes" if symp8 == "True" else "No")
                eits.config(state=DISABLED)

                nin.config(state="normal")
                nin.delete(0,"end")
                nin.insert(0,"Yes" if symp9 == "True"  else "No")
                nin.config(state=DISABLED)

                ten.config(state="normal")
                ten.delete(0,"end")
                ten.insert(0,"Yes" if symp10 == "True"  else "No")
                ten.config(state=DISABLED)

            except Exception as e:

                print(e)
                messageboxx("Info","Don't click on empty space")


        def clear():
            for item in tree.get_children():
                tree.delete(item)


        tree.bind('<ButtonRelease-1>', selectItem)



        root.mainloop()