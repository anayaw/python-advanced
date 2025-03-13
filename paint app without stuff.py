'''
Paint App Project
Author: anaya
Date: mar 7 , 2025

[Project Description]
 im allowing you to paint take it or not !1!1!!!!!111!!1!!!!1!!!!1!
'''
from tkinter import *
from tkinter import colorchooser 
# setup
root = Tk()
root.title("paint !")
f = Frame(root)
f.pack()
c = Canvas(root, bg='white', height=1000, width=1000)
c.pack()


COLOUR = 'black'
SIZE = 10
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black']


class ColourButton():
    def __init__(self, colour):
        self.colour = colour
        self.Button = Button(f, bg=colour, command=self.update)

    def update(self):
        global COLOUR
        COLOUR = self.colour


def colourwindow():
    global COLOUR
    rgb, hex = colorchooser.askcolor(initialcolor='#ff0000')
    COLOUR = hex

def draw_circle(event):
    c.create_oval(event.x, event.y, event.x + SIZE.get(),
                    event.y + SIZE.get(), fill=COLOUR, outline=COLOUR, tags=[COLOUR])
    
def clear_canvas():
    c.delete('all')


colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black']
for i in range(len(colours)):
    x = ColourButton(colours[i])
    x.Button.grid(row=1, column=i)

changecolour= Button(f, text= "change color !!", command= colourwindow)
changecolour.grid(row=0, column= 0)
i = 0
clear_button = Button(f, text='clear !!', command= clear_canvas)
clear_button.grid(row = 0, column = i + 1)

SIZE = IntVar()
scalebar = Scale(f, variable = SIZE, bg = 'grey', tickinterval=1,  resolution = 1, orient = HORIZONTAL, from_ = 1, to = 10)
scalebar.grid(row = 0, column = i + 2)




c.bind("<B1-Motion>", draw_circle) 
root.bind("<q>", quit)
root.mainloop()