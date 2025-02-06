import tkinter as tk
from random import choice
from tkinter import *
root = Tk()

#-------------------------------------------------------------------------------------------
#click me
num = IntVar()
def add():
    num.set(num.get() + 1) # num.get() gets the current value, num.set() will set the value
desc_label = Label(root, text = '✮ how many clicks: ', bg = 'light blue',fg = 'white')
num_label = Label(root, textvariable=num, bg = 'light blue', fg = 'white')
clicker = Button(root, text = '౨ৎ click me !!', bg = 'light blue', fg = 'white', command = add) # see how command is set
desc_label.pack(side = TOP,fill = BOTH)
num_label.pack(side = TOP,fill = BOTH)
clicker.pack(side = BOTTOM,fill = BOTH)
#-------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------
#mouse location
posvar = StringVar()

def update_pos(event): # takes parameter 'event' containing info about the event
    posvar.set('(%d, %d)'%(round(event.x), round(event.y))) # update the posvar variable
loc_label = Label(root, textvariable=posvar, bg = 'light blue', justify = 'center')
loc_label.pack(fill = BOTH)
f = Frame(root, width = 400, height = 400, bg = 'white')
f.pack(side = BOTTOM)
f.bind('<Motion>', update_pos)

#-------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------
#change color 
c = Canvas(root, width = 400, height = 400, bg = 'white')
c.pack(side = BOTTOM)
def change_color(event): # this will be called when event happens
    event.widget.itemconfigure(circle, fill = choice(['light blue','pink','honeydew', 'beige','lavender blush','lavender','antique white']))
circle = c.create_oval(180, 180, 220, 220, fill ='pink',outline="white")
c.tag_bind(circle, '<ButtonPress>', change_color)
# when ButtonPress (mouse click) happens on c, call change_colour

#-------------------------------------------------------------------------------------------

root = mainloop()
