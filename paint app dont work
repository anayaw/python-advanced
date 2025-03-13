'''
Paint App Project
Author: anaya
Date: mar 7 , 2025

[Project Description]
 im allowing you to paint take it or not !1!1!!!!!111!!1!!!!1!!!!1!
'''

from tkinter import *

''''
Your window has been created for you.
TODO:
- create your frame
- create your canvas

'''
root = Tk()
root.title('paintt')

c = Canvas(root,bg="white", height=1000, width=1000)
f = Frame(root, bg="white",height=600,width=600)
c.pack()
f.pack()


'''
This project will use some global variables.
COLOUR represents the current colour being used, and
SIZE is the current size of the paintbrush.
'''
COLOR = 'black'
SIZE = 10
colors= ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

class ColorButton():
     '''
     A ColourButton is the class for the buttons at the
     top of the screen that change the brush colour.
     '''
     def __init__(self, color):
          '''
          This is the function called when creating a ColourButton.
          TODO:i done yayayay 244 !1!1!1!!
          - fill in the line indicated below.
          '''
          self.color = color
          self.Button = Button(f, bg=color, command=self.update) 
     
     def update(self):
          '''
          This is the method that is the command for a ColourButton.

          When a ColourButton is pressed, it must ONLY change the global COLOUR
          variable to be this ColourButton's colour attribute/
          TODO:
          - fill in this function. It should be 2 lines. i done
          '''
          global COLOR
          COLOR = self.color
     
def draw_circle(event):
    '''
    This function is called whenever the user is dragging their mouse on the
    canvas. Use the canvas method 'createoval' to draw a circle there.
    Remember to refer to your global variables to draw the correct circle.
    TODO:
    - finish this function (should be 1-2 lines)
    '''
    c.create_oval(event.x, event.y, event.x + SIZE.get(), event.y + SIZE.get(), fill= COLOR, outline= COLOR)
    
def clear_canvas():
    '''
    This function is called whent the user presses the CLEAR button.
    It must clear all drawings from the canvas.
    TODO:
    - finish this function (1 line)
    
    '''
    c.delete('all')

#################### MAIN CODE #########################

'''
Here we first are making the ColourButtons. We will do this in a quick
and expandable way using a list. Add all the colours you want buttons for
to the list 'colours'.
The for loop will create the ColourButton objects.
TODO:
- add at least 4 more colours to the colours list
'''

colors= ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
for i in range(len(colors)):
    x = ColorButton(colors[i])
    x.Button.grid(row=0, column=i)

'''
Next create the CLEAR button and the width slider.

TODO:
- complete the code fragments below
'''
clear_button = Button(f, text='clear', command= clear_canvas)
clear_button.grid(row = 0, column = i + 1)

SIZE = IntVar()
'''# We are using the global variable as the int var so it is always updated'''
scalebar = Scale(f, variable = SIZE, bg = 'grey', tickinterval=1,  resolution = 1, orient = HORIZONTAL, from_ = 1, to = 10)
scalebar.grid(row = 0, column = i + 2)

'''
TODO:
- bind the event of mouse button held down while moving ON THE CANVAS to the draw_circle function
- bind the letter q to quitting the program
- mainloop!
'''
c.bind("<B1-Motion>", draw_circle) 
root.bind("<q>", quit)
root.mainloop()
