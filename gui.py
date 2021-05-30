# code to add gui for the main code

from tkinter import *

def calc(event):
    label.config(text="Result: " + str(eval(entry.get())))

root = Tk()
root.title("Hello")
root.geometry("300x200+100+100")
root.resizable(False, False)

label = Label(root, text="0")
label.pack()

entry = Entry(root, width=30)
entry.bind("<Return>", calc)
entry.pack()

root.mainloop()
