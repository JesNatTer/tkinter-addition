import tkinter as tk
from tkinter import *

root = tk.Tk()

root.geometry("600x200")


def add_numbers():
    res = int(e1.get())+int(e2.get())
    label_text.set(res)


def delete():
    e1.delete(1)
    e2.delete(1)


label_text = StringVar()
Label(root, text="enter first number:").grid(row=0, sticky=W)
Label(root, text="Enter second number:").grid(row=1, sticky=W)
Label(root, text="result of addition:").grid(row=3, sticky=W)
result = Label(root, text="", textvariable=label_text).grid(row=3, column=1, sticky=W)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b = Button(root, text="Add", command=add_numbers)
b1 = Button(root, text="Clear", command=delete())
b2 = Button(root, text="Exit", command=root.destroy)
b.grid(row=5, column=1, sticky=W+E+N+S, padx=5, pady=5)
b1.grid(row=5, column=2, sticky=W+E+N+S, padx=5, pady=5)
b2.grid(row=5, column=3, sticky=W+E+N+S, padx=5, pady=5)

root.mainloop()
