from tkinter import *

root = Tk()

c = Canvas(root, height=500, width=500, bg="light blue")


# c.create_line(50,50,450,50)
# c.create_line(450,50,50,450)
# c.create_line(50,450,450,450)
# c.create_line(450,450,50,50)

# c.create_rectangle(150,50,350,450)
# c.create_oval(200,100,300,300)
# c.create_polygon(210, 285, 175, 200, 260, 225, fill='white')
# c.pack()
c.create_rectangle(50, 50, 550, 550, fill="light blue",
tags=('frame'))
c.create_polygon(210, 285, 175, 200, 260, 225, fill='brown',
outline='black', tags=('ears'))
c.create_oval(200, 200, 400, 400, fill="brown", tags=('head'))
c.create_line(300, 350, 325, 370, tags=('mouth'))
c.create_polygon()
c.pack()
root.mainloop()