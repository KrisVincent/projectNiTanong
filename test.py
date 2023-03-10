import tkinter as tk
root = tk.Tk()
root.geometry("400x50")

def setTextInput(text):
    textExample.delete(0,"end")
    textExample.insert(0, text)

textExample = tk.Entry(root)
textExample.pack()

btnSet = tk.Button(root, height=1, width=10, text="Set",
                    command=lambda:setTextInput("new content"))
btnSet.pack()

root.mainloop()