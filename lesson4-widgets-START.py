'''
Project Title: something idk
Author: anaya
Date: september 5, 2024

[insert description of project and instructions for use]
idk ig its a quiz i didnt see :3
'''


'''
TODO:
- fill out titleblock
- create at least 5 questions
    - each question requires:
        - it's own frame
        - a label to ask the question (in this frame)
        - a widget to get input (in this frame) ex. Button, Entry, RadioButton

- each question must use a different type of widget for input - Get creative!
- stylize the test to show off what you know! Use background and foreground
colours, alignment settings, images, frame padding etc. to make it appealing

'''


from tkinter import *
root = Tk()

# These lists will hold each of your StringVars (1 per question)
# and expected answers (1 per question)
# As you create your questions, append to these lists so that stringvars[i]
# is considered correct if it's value is equal to answers[i]
stringvars = []
answers = []

result = StringVar()

    
def check_answers():
    points = 0
    for i in range(len(answers)):
        if stringvars[i].get() == answers[i]:
            points += 1
    result.set(str(points))

# Add all your questions and widgets here
#question 1 .. 😨😨
f = Frame(root,height=450,width=450,bg="pink")
f.pack()
l1=Label(f,text="who is my favorite sanrio character 🥰 ??")
l1.pack()

q1 = StringVar()
a = Radiobutton(f,text='hello kitty', variable=q1, value='hello kitty')
b = Radiobutton(f,text="my melody",variable=q1,value='my melody')
c = Radiobutton(f,text="kuromi",variable=q1,value='kuromi')
d = Radiobutton(f,text='chococat',variable=q1,value='chococat')
a.pack()
b.pack()
c.pack()
d.pack()
answers.append('hello kitty')
stringvars.append(q1)

#question 2
f1 = Frame(root,height=450,width=450,bg="pink")
f1.pack()
l2=Label(f1,text="whats my fav video game (。・ω・。)")
l2.pack()

q2 = StringVar()
a = Checkbutton(f1,text="minecraft",variable=q2, onvalue="1", offvalue="0")
b = Checkbutton(f1,text='fortnite',variable=q2, onvalue="2", offvalue="0")
c = Checkbutton(f1,text="roblox",variable=q2, onvalue="3", offvalue="0")
a.pack()
b.pack()
c.pack()
answers.append("3")
stringvars.append(q2)

#question 3
f2 = Frame(root,height=450,width=450,bg="pink")
f2.pack()
l3=Label(f2,text="whats my fav food (★‿★) ??")
l3.pack()
wowie = StringVar()
a = Entry(f2,textvariable=wowie)
a.pack()
answers.append("fries")
stringvars.append(wowie)


#question 4
s = StringVar()

def oldd():
     global s
     s.set("22 or 23")
     answers.append("22 or 23")
     stringvars.append(s)
def youngg():
     global s
     s.set("5 or 6")
     answers.append("5 or 6")
     stringvars.append(s)
def good():
     global s
     s.set("11 or 12")
     answers.append("11 or 12")
     stringvars.append(s)

f3 = Frame(root,height=450,width=600,bg="light yellow")

l4=Label(f3,text="whats my age 🥰😡😡")
l4.pack()

old= Button(f3,text="22 or 23",command=oldd,fg="pink",state="active")
young= Button(f3,text="5 or 6",command=youngg,fg="light blue",state="active")
good_job= Button(f3,text="11 or 12",command=good,fg="yellow",state="active")
old.pack()
young.pack()
good_job.pack()
f3.pack()
# This submit button should be at the end of your test
# It is meant to be clicked once the user has answered all questions
submitButton = Button(root, text='Submit Answers',
                      bg='white', command=check_answers)
submitButton.pack()

# This results label will display the number of questions answered correctly
# Feel free to change up the code for submitButton and results to make
# the test prettier and individualized!
results = Label(root, textvariable=result)
results.pack()

root.mainloop()
