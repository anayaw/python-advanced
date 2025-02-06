import tkinter as tk
from tkinter import *
from tkcalendar import DateEntry
root = Tk()


#name
f=Frame(root,bg="pink",height=600,width=600)
f.pack()
l2 = Label(f, text='name:', bg='pink', fg='white', justify='center')
l2.pack()


text = Text(f, width=40, height=2,background = 'pink')
text.pack()
#birthday
f2=Frame(root,background="light blue",height=600,width=600)
f2.pack()
l1 = Label(f2, text='birthday:', bg='light blue', fg='white', justify='center')
l1.pack()
cal = DateEntry(root, width=12, year=2024, month=6, day=22, background='lightblue', foreground='white', borderwidth=2)
cal.pack(padx=10, pady=10)

#phone numba
f1=Frame(root,bg="light blue",height=600,width=600)
f1.pack()
l1 = Label(f1, text='phone numba:', bg='light blue', fg='white', justify='center')
l1.pack()

text = Text(f1, width=40, height=2,background = 'light blue')
text.pack()
#def get_scale_value():
#    value = scale.get()  # Get the current value of the scale
#    print(f"Selected value: {value}")
#scale = tk.Scale(root, bg="light blue", from_=0, to=100, orient=tk.HORIZONTAL)  # Horizontal scale from 0 to 100
#scale.pack(padx=20, pady=20)
#button = tk.Button(root, bg="light blue", text="Get Scale Value", command=get_scale_value)
#button.pack(padx=20, pady=10)
# text.pack()
root.mainloop()