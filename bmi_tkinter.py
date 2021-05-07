import tkinter as tk
from tkinter import *

root = tk.Tk()

root.title("BMI Calculator")

root.geometry("900x300")

frame1 = Frame(root, width="300", height="100", bd="2", relief="flat")
frame1.pack()
frame2 = Frame(root, width="300", height="100", bd="2", relief="raised")
frame2.pack()
frame3 = Frame(root, width="300", height="100", bd="2", relief="raised")
frame3.pack()


genderoptions = ["Male", "Female"]

value_inside = StringVar(root)

value_inside.set("select gender")


def bmi():
    weight = int(w.get())
    height = int(h.get())
    res1 = float(weight / (height/100)**2)
    lbmi = Label(frame3, text=bmi)
    lbmi.pack(side=BOTTOM)
    res1 = str(res1)


def maleidealbmi():
    res2 = 0.5 * w.get() / ((h.get()/100)**2) + 11.5


def femaleidealbmi():
    res3 = 0.5 * w.get()/((h.get()/100)**2) + 0.03 * a.get() + 11


def gndr(selection):
    g = selection

def reslt():
    if value_inside.get() == "Male" or value_inside.get() == "Female":
        lbmi = Label(frame3, text=bmi)
        lbmi.pack(side=BOTTOM)
    else:
        errorl = Label(frame3, text="Error")
        errorl.pack(side=BOTTOM)


label = Label(frame1, text='Calculate your BMI')
label.pack()
lweight = Label(frame2, text="Weight in Kg:")
lweight.pack()
lheight = Label(frame2, text="Height in cm:")
lheight.pack()
lgender = Label(frame2, text="Gender:")
lgender.pack()
lage = Label(frame2, text="Age:")
lage.pack()

w = Entry(frame2)
w.pack()

h = Entry(frame2)
h.pack()

gender = OptionMenu(frame2, value_inside, *genderoptions)
gender.pack(side=TOP)

a = Entry(frame2)
a.pack()

result = Button(frame3, text="Your BMI", command=bmi)
result.pack()


root.mainloop()

