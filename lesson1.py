from tkinter import *
'''
Project Name:cat
Author:caat
Date:2024-06-20

This is a title block! Title blocks help you keep track of the purpose and 
progress of a project. We will be including one at the beginning of all projects
from now on.

After filling out the 3 pieces of information, write a short blurb on 
what this project does and how to use it! This only needs to be two sentences
for this simple project.
'''


'''
TODO:
- create a canvas with a
    - background colour
    - size

- using lines, polygons, rectangles, and ovals, draw an animal on your canvas
- tag all your canvas objects!
'''




from tkinter import *
def print_loc(event):
    '''
    This function is made for you to help you get familiar with the grid on the
    screen!

    It will print out the X, Y coordinates of any point you want.
    When your program is running, simply click (using left moust button)
    on the point on the canvas you want the location of.
    The output will be in the shell!

    '''
    print(event.x, event.y)


# Your window has been made for you below
root = Tk()

# this line allows our print function to be called when and wherever you click
root.bind("<Button-1>", print_loc)

# Create your canvas and all your canvas objects here! Don't forget to pack!
c = Canvas(root,height=600,width=600, bg='light yellow')
c.create_rectangle(50, 50, 550, 550, fill="light blue",tags=('frame'))
c.create_polygon(210, 285, 175, 200, 260, 225, fill='brown',outline='black', tags=('ears'))
c.create_polygon(210,285,175, 200,225,245, fill = 'white', outline='black',tags=("more ear"))
c.create_polygon(413,184,388,253,345,211,fill='brown',outline='black', tags=('ears'))
c.create_polygon(413,184,388,253,366,231,fill="white",outline='black',tags=('more ears'))
c.create_oval(200, 200, 400, 400, fill="brown", tags=('head'))
c.create_oval(310,260,370,320, fill="white", tags=('eyes'))
c.create_oval(230,260,290,320, fill="white", tags=('eyes'))
c.create_oval(320,290,350,320, fill="black", tags=('pupiles'))
c.create_oval(250,290,280,320, fill="black", tags=('pupiles'))
c.create_oval(290, 330,310,350,fill="pink", tags=('nose'))
c.create_line(300, 350, 325, 370, tags=('mouth'))
c.create_line(300, 350, 275, 370, tags=('mouth'))
c.pack()
# Do not remove this line! It keeps your window open while the code is running
root.mainloop()
