import tkinter as tk
from tkinter import *

# q1
dict = {'Shivangi': '456737847', 'Ria': '9394839783', 'Tina': '7366384683', 'Pia': '98938985', 'Rohit': '89489484',
        'Mina': '287289472'}
c = tk.Tk()
f = Frame(master=c)
f.pack()
scroll = Scrollbar(master=f)
scroll.pack(fill=Y, side=RIGHT)
l = Listbox(f, yscrollcommand=scroll.set)
l.pack()
for key in dict:
    l.insert(END, '{}'.format(key))


# q2
def add():
    dict.update({a.get(): b.get()})
    for key in dict.keys():
        print(key)
    i = key
    l.insert(END, i)


bu = Button(master=f, text="Add", command=add)
bu.pack()
la = Label(f,text="Enter the name and phone number:")
la.pack()
a = Entry(f, text="Name")
b = Entry(f, text="Phone no")
a.pack()
b.pack()
c.mainloop()
