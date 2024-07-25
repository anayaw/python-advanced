from tkinter import *
root = Tk()
c = Canvas(root, width=600, height=600, bg='pink')


# f = Frame(root, height=200, width=200, bg='grey') # simplest object creation


# img= PhotoImage(file="Hello_Kitty.png")

# l1= Label(f, image=img)
# l2=Label(f,text="wow its hello kitty :3 woowowwowwowoowowowo")
b = Button(c,text="hello kitty?")
def yay():
    print("HELLO KITTY :D")
b1 = Button(c,text="hihih",command=yay,fg="pink",state="active")


a = StringVar()
b2=Checkbutton(c,text="did the dog fly",variable=a)

release = StringVar()
ra = Radiobutton(c,text="yes",variable=release,value=0)
rb = Radiobutton(c,text="no",variable=release,value=1)
rc = Radiobutton(c,text="maybe",variable=release,value=6)

textbox = StringVar()
entrybox = Entry(c,show="*",textvariable=textbox)
entrybox.pack()


l3 = Label(c,text="joe",bg="grey",justify="center")
val = l3.cget("justify")
print(val)



ra.pack()
rb.pack()
rc.pack()
b.pack()
b1.pack()
b2.pack()



# l2.pack()
# l1.pack()
# f.pack()
c.pack()
root.mainloop()