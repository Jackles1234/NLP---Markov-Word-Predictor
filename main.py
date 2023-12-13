from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import model

def text_edited(e):
    print('Current text:',inputtxt.get(1.0,tk.END))
    print(e.keysym, ' was pressed')


def my_after(): 
    new_text = inputtxt.get(1.0,tk.END)
    print(new_text)
    temp1, temp2, temp3 = model.generate_next(new_text)
    l2.config(text=temp1[1:])
    l3.config(text=temp2[1:])
    l4.config(text=temp3[1:])


    # call again after 100 ms
    root.after(1000, my_after)

root = Tk()
root.geometry("1000x800")
root.title(" Text Predictor ")

def append_string(temp):
    inputtxt.insert(tk.END, temp)


l = Label(text = "Enter your text")
inputtxt = Text(root, height = 17,
                width = 65,
                bg = "light yellow")
Display1 = Button(root,
                 text ="Show",
                 command = lambda:append_string(l2.cget("text")[1:]))
l2 = Label(text = "")

Display2 = Button(root,
                 text ="Show",
                 command = lambda:append_string(l3.cget("text")[1:]))
l3 = Label(text = "")

Display3 = Button(root,
                 text ="Show",
                 command = lambda:append_string(l4.cget("text")[1:]))
l4 = Label(text = "")




l.grid(row = 0, column = 0)
inputtxt.grid(row = 1, column = 2)
inputtxt.bind(text_edited)
Display1.grid(row = 3, column = 1)
l2.grid(row = 4, column = 1)
Display2.grid(row = 3, column = 2)
l3.grid(row = 4, column = 2)
Display3.grid(row = 3, column = 3)
l4.grid(row = 4, column = 3)

my_after()
mainloop()