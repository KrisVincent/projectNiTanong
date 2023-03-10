#pip3 install keyboard
from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar
import sqlite3
import cv2
import PIL
from PIL import Image, ImageTk
import io




class form_window:

    def __init__(self):

        root = Tk()
        root.geometry("800x600")
        root.title("Contact Tracer Form")

        get_first_name = StringVar()
        get_last_name = StringVar()
        get_middle_name = StringVar()
        get_temperature = StringVar()
        get_address = StringVar()
        get_email = StringVar()
        get_contact_number = StringVar()
        get_gender = StringVar()
        get_date = StringVar()


        width, height = 200, 200
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        lmain = Label(root)
        lmain.pack()
        lmain.place(x=460, y=340)

        #for pictures
        def show_frame():
            _, frame = cap.read()
            frame = cv2.flip(frame, 1)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

            img = PIL.Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)

            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(10, show_frame)

            return imgtk

        def capture(imgtk):

            imgpil = ImageTk.getimage(imgtk)
            if imgpil.mode in ("RGBA", "P"):
                im = imgpil.convert("RGB")
            im.save("123.jpg", quality=100, subsampling=0)

            byteIO = io.BytesIO()
            im.save(byteIO, format='PNG', quality=95)
            get_file = byteIO.getvalue()

            return get_file

        show_frame()

        headerTitle = Label(root, text="DHVSU Contact Tracer")
        headerTitle.pack()
        headerTitle.place(x=350, y=10)

        lnameEntry = Entry(root, textvariable=get_last_name)
        lnameEntry.pack()
        lnameEntry.place(x=25, y=80)

        fnameEntry = Entry(root, textvariable=get_first_name)
        fnameEntry.pack()
        fnameEntry.place(x=158, y=80)

        midInitialEntry = Entry(root, textvariable=get_middle_name, width=5)
        midInitialEntry.pack()
        midInitialEntry.place(x=290, y=80)

        mailEntry = Entry(root, textvariable=get_email, width=40)
        mailEntry.pack()
        mailEntry.place(x=25, y=165)

        numEntry = Entry(root, width=20, textvariable=get_contact_number)
        numEntry.pack()
        numEntry.place(x=279, y=165)

        maleRadio = Radiobutton(root, text="Male", variable=get_gender, value="male")
        maleRadio.pack()
        maleRadio.place(x=340, y=90)

        femaleRadio = Radiobutton(root, text="Female", variable=get_gender, value="female")
        femaleRadio.pack()
        femaleRadio.place(x=340, y=70)

        tempEntry = Entry(root, textvariable=get_temperature, width=5)
        tempEntry.pack()
        tempEntry.place(x=420, y=80)

        addEntry = Entry(root, textvariable=get_address, width=62)
        addEntry.pack()
        addEntry.place(x=25, y=125)

        calendarLabel = Label(root, text="Your BirthDate:")
        calendarLabel.pack()
        calendarLabel.place(x=540, y=90)

        pickDate = Calendar(root, textvariable=get_date, selectmode='day')
        pickDate.place(x=470, y=120)

        surnameLabel = Label(root, text="Surname")
        surnameLabel.pack()
        surnameLabel.place(x=25, y=55)

        firstnameLabel = Label(root, text="Firstname")
        firstnameLabel.pack()
        firstnameLabel.place(x=158, y=55)

        miLabel = Label(root, text="M.I.")
        miLabel.pack()
        miLabel.place(x=293, y=55)

        genderLabel = Label(root, text="Gender")
        genderLabel.pack()
        genderLabel.place(x=345, y=55)

        tempLabel = Label(root, text="Temp (celcius)")
        tempLabel.pack()
        tempLabel.place(x=420, y=55)

        addLabel = Label(root, text="Complete Address:")
        addLabel.pack()
        addLabel.place(x=25, y=103)

        mailLabel = Label(root, text="Email Address:")
        mailLabel.pack()
        mailLabel.place(x=25, y=143)

        numLabel = Label(root, text="Contact Number:")
        numLabel.pack()
        numLabel.place(x=279, y=143)

        travelLabel = Label(root, text="TRAVEL HISTORY")
        travelLabel.pack()
        travelLabel.place(x=25, y=220)

        THone = Label(root, text="1. Did you travel to Metro Manila within 14 days?")
        THone.pack()
        THone.place(x=25, y=240)

        radio_var1 = BooleanVar()
        radio_var2 = BooleanVar()
        radio_var3 = BooleanVar()


        thoneYES = Radiobutton(root, text="Yes", variable=radio_var1, value=True)
        thoneYES.pack()
        thoneYES.place(x=50, y=260)

        thoneNO = Radiobutton(root, text="No", variable=radio_var1, value=False)
        thoneNO.pack()
        thoneNO.place(x=120, y=260)

        THtwo = Label(root, text="2. Did you visit other country one month before coming to this facility?")
        THtwo.pack()
        THtwo.place(x=25, y=290)

        thtwoYES = Radiobutton(root, text="Yes", variable=radio_var2, value=True)
        thtwoYES.pack()
        thtwoYES.place(x=50, y=310)

        thtwoNO = Radiobutton(root, text="No", variable=radio_var2, value=False)
        thtwoNO.pack()
        thtwoNO.place(x=120, y=310)

        THthree = Label(root, text="3. Did you encounter someone who is porbable , suspected and positive")
        THthree.pack()
        THthree.place(x=25, y=330)

        ththree = Label(root, text=" case within 14 days?")
        ththree.pack()
        ththree.place(x=33, y=345)

        ththreeYES = Radiobutton(root, text="Yes", variable=radio_var3, value=True)
        ththreeYES.pack()
        ththreeYES.place(x=50, y=360)

        ththreeNO = Radiobutton(root, text="No", variable=radio_var3, value=False)
        ththreeNO.pack()
        ththreeNO.place(x=120, y=360)

        symptompsLabel = Label(root, text="SYMPTOMS")
        symptompsLabel.pack()
        symptompsLabel.place(x=25, y=400)

        fstsymptom = Label(root, text="-Fever")
        fstsymptom.pack()
        fstsymptom.place(x=25, y=420)

        scndsymptom = Label(root, text="-Sore Throat")
        scndsymptom.pack()
        scndsymptom.place(x=25, y=440)

        trdsymptom = Label(root, text="-Cough")
        trdsymptom.pack()
        trdsymptom.place(x=25, y=460)

        frtsymptom = Label(root, text="-Cold")
        frtsymptom.pack()
        frtsymptom.place(x=25, y=480)

        fifsymptom = Label(root, text="-Chills")
        fifsymptom.pack()
        fifsymptom.place(x=25, y=500)

        sixsymptom = Label(root, text="-Skin Rashes")
        sixsymptom.pack()
        sixsymptom.place(x=250, y=420)

        sevsymptom = Label(root, text="-Body Pain")
        sevsymptom.pack()
        sevsymptom.place(x=250, y=440)

        eitsymptom = Label(root, text="-Loss of Appetite ")
        eitsymptom.pack()
        eitsymptom.place(x=250, y=460)

        ninsymptom = Label(root, text="-Loss of Smell")
        ninsymptom.pack()
        ninsymptom.place(x=250, y=480)

        tensymptom = Label(root, text="-Loss of Taste")
        tensymptom.pack()
        tensymptom.place(x=250, y=500)

        #variables
        symp1 = StringVar()
        symp2 = StringVar()
        symp3 = StringVar()
        symp4 = StringVar()
        symp5 = StringVar()
        symp6 = StringVar()
        symp7 = StringVar()
        symp8 = StringVar()
        symp9 = StringVar()
        symp10 = StringVar()

        symptom1 = Checkbutton(root, variable=symp1, onvalue="True", offvalue="False")
        symptom1.pack()
        symptom1.deselect()
        symptom1.place(x=140, y=420)

        symptom2 = Checkbutton(root, variable=symp2, onvalue="True", offvalue="False")
        symptom2.pack()
        symptom2.deselect()
        symptom2.place(x=140, y=440)

        symptom3 = Checkbutton(root, variable=symp3, onvalue="True", offvalue="False")
        symptom3.pack()
        symptom3.deselect()
        symptom3.place(x=140, y=460)

        symptom4 = Checkbutton(root, variable=symp4, onvalue="True", offvalue="False")
        symptom4.pack()
        symptom4.deselect()
        symptom4.place(x=140, y=480)

        symptom5 = Checkbutton(root, variable=symp5, onvalue="True", offvalue="False")
        symptom5.pack()
        symptom5.deselect()
        symptom5.place(x=140, y=500)

        symptom6 = Checkbutton(root, variable=symp6, onvalue="True", offvalue="False")
        symptom6.pack()
        symptom6.deselect()
        symptom6.place(x=390, y=420)

        symptom7 = Checkbutton(root, variable=symp7, onvalue="True", offvalue="False")
        symptom7.pack()
        symptom7.deselect()
        symptom7.place(x=390, y=440)

        symptom8 = Checkbutton(root, variable=symp8, onvalue="True", offvalue="False")
        symptom8.pack()
        symptom8.deselect()
        symptom8.place(x=390, y=460)

        symptom9 = Checkbutton(root, variable=symp9, onvalue="True", offvalue="False")
        symptom9.pack()
        symptom9.deselect()
        symptom9.place(x=390, y=480)

        symptom10 = Checkbutton(root, variable=symp10, onvalue="True", offvalue="False")
        symptom10.pack()
        symptom10.deselect()
        symptom10.place(x=390, y=500)

        sendButton = Button(root,
                            width=10,
                            text="Send",
                            font=("Arial", 10),
                            command=lambda:
                            buttonclick()
                            ).place(x=300, y=520)

        adminButton = Button(root,
                            width=10,
                            text="Admin",
                            font=("Arial", 10),
                            command=lambda:
                            adminClicked()
                            ).place(x=200, y=520)

        #fucntion stuff below

        def adminClicked():

            import login_window
            login_window.login(root).get_window()




        def buttonclick():

            result = messagebox.askquestion("Confirm", "Are you sure?")

            if result == "yes":

                print(f"Fname:{get_first_name.get()}")
                print(f"Lname:{get_last_name.get()}")
                print(f"Fname:{get_middle_name.get()}")
                print(f"Gender: {get_gender.get()}")
                print(f"Temp:{get_temperature.get()} celcius")
                print(f"address:{get_address.get()}")
                print(f"email:{get_email.get()}")
                print(f"contact:{get_contact_number.get()}")
                print(get_date.get())

                print(radio_var1.get())
                print(radio_var2.get())
                print(radio_var3.get())

                capture(show_frame())

                conn = sqlite3.connect("contact_tracerDB.db")

                cursor = conn.cursor()
                file = capture(show_frame())

                cursor.execute("INSERT INTO respondents_data("
                               "surname, firstname, MI,gender,temperature,address,email,number,birthday,user_picture) "
                               "VALUES (? ,? ,?, ?,?,?,?,?,?,?)",

                               (
                               get_last_name.get().upper(), get_first_name.get().upper(), get_middle_name.get().upper(),
                               get_gender.get(), get_temperature.get(), get_address.get().upper(), get_email.get(),
                               get_contact_number.get(), get_date.get(), file))

                conn.commit()

                cursor.execute("INSERT INTO respondents_syndrome("
                               "fever,sore_throat,cough,cold,chills,skin_rashes,body_pain,"
                               "loss_of_appetite,loss_of_smell,loss_of_taste)"
                               "VALUES (? ,? ,?, ?,?,? ,? ,?, ?,?)",

                               (symp1.get(), symp2.get(), symp3.get(), symp4.get(), symp5.get()
                                , symp6.get(), symp7.get(), symp8.get(), symp9.get(), symp10.get()))

                conn.commit()



                cursor.execute("INSERT INTO respondents_travel_history("
                               "question_1,question_2,question_3)"
                               "VALUES (? ,? ,?)",

                               (radio_var1.get(), radio_var2.get(), radio_var3.get()))

                conn.commit()

                messagebox.showinfo("Info","Data Succesfully Uploaded!")

                refresh(self)



            else:
                print("Send Cancelled")

        #basically reset
        def refresh(self):
            root.destroy()
            self.__init__()

        root.mainloop()


