import tkinter as tk
from tkinter import *
import sys
def helloCallBack():
   print("This is a tkinter program")


# q1
c = tk.Tk()
l = Label(c, text="Hello World")
l.pack()
w = tk.Button(c, text="exit",command=ends())
w.pack()
c.mainloop()

#q2

p = tk.Button(c, text="Message",command=helloCallBack())
p.pack()
c.mainloop()

#q3
def change(w):
    w.configure(text="TEXT CHANGED")
    w.grid()
r=tk.Tk()
f=tk.Frame(r)
f.pack()
w= Label(master=f,text="Parks and Recreation")
w.grid(row=1)
b= Button(master=f,text="exit",command=sys.exit())
b.grid(row=2, column=1)
b2= Button(master=f, text="Change Message",command=change(w))
b2.grid(row=2, column=2)
r.mainloop()

#q4
def other():
    res = w.get()
    fin.config(text=res)
    w.delete(0, END)

r=tk.Tk()
f=tk.Frame(r)
f.pack()
w=Entry(f)
w.bind()
enter = Button(r, text="Enter your text", command=other)
enter.pack()
fin = Label(r, text="", bg="blue")
fin.pack()
r.mainloop()

