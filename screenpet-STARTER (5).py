'''
Project: Screen Pet
Author: anaya ⭐ 
Date : aw man does it matter ? (2025-02-06 , 5:44 pm now 5:45)

[Project Description]
literally a cat thats animated 

how are you doing that 😨 ?? bang bang bang 😁 
'''

'''
TODO:
1. Copy over your screen pet drawing here to animate it! (Or you can make a new one if you wish)

⭐⭐
def print_loc(event):
   
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
⭐⭐

2. Decide on at least 3 events and their corresponding actions
    EXAMPLES
    - Draw a set of closed eyes, and opened eyes. Pet blinks automatically. Pet winks if eyes clicked. ⭐
    - Draw an exaggerated smile. Pet switched mouth to smile if user moves mouse over face. ⭐
    - On activation (when window is created) Pet smiles / Any action
    - A pet's feature (ex. nose, ears) changes colour when clicked ⭐
'''

'''
HOW TO CREATE ALTERNATE VERSIONS:
1. Create a variable storing version 1, set state to NORMAL
2. Create a variable storing version 2, set state to HIDDEN
    This will create the object, but not place it on the screen.

HOW TO SWITCH BETWEEN THE VERSION:
1. Create a function that toggles
    1.1. Figure out which version is currently in use
        - do this using a global variable that keeps track of this OR
        - fetch the current state of the canvas object involved ex. if the variable for verson 1's state is HIDDEN (using c.itemcget function)
    1.2  Switch the state for the version in use to HIDDEN
    1.3  Switch the state for the other version to NORMAL - if using a global variable, change it now
2. Ensure this function is bound to the appropriate event
(EXAMPLE GIVEN - crossed and uncrossed version of eyes)

'''

'''
HOW TO MAKE ACTIONS OCCUR AUTOMATICALLY - TIMED
If you want func_a function to happen every second, in the function definition, write
root.after(1000, func_a) <- this tells the root to call this function again after 1000 milliseconds
Ensure function is called once in the main code.
(EXAMPLE GIVEN - crossing and uncrossing eyes is done automatically)

'''
from tkinter import *
root = Tk()

c = Canvas(root, width=600, height=600, bg='light blue')
crossed = False  # Starting out with uncrossed eyes

c.create_rectangle(50, 50, 550, 550, fill="light yellow",
tags=('frame'))
left_ear=c.create_polygon(395, 285, 420, 200, 340, 225, fill = 'brown', outline='black', tags=('ears'))
right_ear=c.create_polygon(210, 285, 175, 200, 260, 225, fill='brown', outline='black', tags=('ears'))
inner_left_ear=c.create_polygon(210, 285, 175, 200, 215, 250, fill='white',outline='black', tags=('Inner ear'))
inner_right_ear=c.create_polygon(395, 290, 420, 200, 390, 251, fill = 'white', outline='black', tags=('Inner ears'))
head = c.create_oval(200, 200, 400, 400, fill="brown", tags=('head'))
c.create_line(300, 350, 325, 370, tags=('mouth'))
c.create_line(300, 350, 275, 370, tags=('mouth'))
c.create_oval(282, 318, 318, 348, fill="pink", tags=('nose'))
left_eye_white=c.create_oval(230, 273, 280, 328, fill = 'white', tags='eye')
right_eye_white=c.create_oval(315, 273, 365, 328, fill = 'white', tags='eye on right')

def toggle_eyes():
    '''
    If using a global variable, include lines like this to 
    use and check that variable

    global crossed
    if not crossed:
    '''
    # This function uses the approach of checking an object's state to determine what version is currently used
    if c.itemcget(left_eye_pupil_1, 'state') == NORMAL:
        c.itemconfigure(left_eye_pupil_1, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_1, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_2, state=NORMAL)
        c.itemconfigure(right_eye_pupil_2, state=NORMAL)
        '''crossed = True # this is ESSENTIAL if using the global variable approach'''

    else:
        c.itemconfigure(left_eye_pupil_2, state=HIDDEN)
        c.itemconfigure(right_eye_pupil_2, state=HIDDEN)

        c.itemconfigure(left_eye_pupil_1, state=NORMAL)
        c.itemconfigure(right_eye_pupil_1, state=NORMAL)
        '''crossed = False'''

    # after 1000 milliseconds, call this function again
    root.after(1000, toggle_eyes)

# Normal pupils - the tags here haven't been used in this example but they may be helpful for other events
left_eye_pupil_1 = c.create_oval(248, 293, 280, 328, fill = 'black', tags='pupil')
right_eye_pupil_1 = c.create_oval(315, 293, 348, 328, fill = 'black', tags='pupil on right')

# Crossed eye pupils
left_eye_pupil_2 = c.create_oval(228, 271, 260, 308, fill='black', tags=('eye', 'pupil', 'crossed'), state=NORMAL)
right_eye_pupil_2 = c.create_oval(315, 271, 348, 308, fill='black', tags=('eye', 'pupil', 'crossed'), state=NORMAL)

toggle_eyes()  # function must be called once in the main code to start the automatic process




c.pack()
root.mainloop()

