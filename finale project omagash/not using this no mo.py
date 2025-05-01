# anaya idea $$$
''' oka so like pizza where you make it and put it in box and serve  '''
'''i choosy memory quiz game which isn't rlly a memory quiz game but its more of a trivia and now you're just reading this is kinda boring and honestly i wanna go sleep sleep but oh welll it not matter hehehe oaky byebey'''

from tkinter import  *
from tkinter import messagebox
from tkinter import filedialog
root = Tk()
#these make life of python

# stringvar = []
# answerss = []
# result = stringvar()
#q n a hehehe

c = Canvas(root, height=600, width=600, bg="light blue")
f = Frame(root, height=300, width=300, bg="light yellow")
#this is my stuff to start the whole code or else it would be bad w / o it

def saveas():
    save_filename = filedialog.asksaveasfilename()

def on_exit():
    if messagebox.askokcancel("quits", "do you want to quit??"):
        root.destroy()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="leabes", command=on_exit)
filemenu.add_separator()
filemenu.add_command(label="saves (good job , save it)", command=saveas)
menubar.add_cascade(label="file :0", menu=filemenu)
root.config(menu=menubar)

# menubar = Menu(root)
# menu_leabepls = Menu(menubar) 
# menubar.add_cascade(menu=menu_leabepls, label='if you dont wanna be in this file anymore but OH NO the x button isnt working')
# menu_leabepls.add_command(label='leaves yipe')
# root.config(menu = menubar)

#this is menu, you may leavee




root.mainloop()
#the end of this very interesting projectt 1!1!1!1!!!!1!!1!1!!