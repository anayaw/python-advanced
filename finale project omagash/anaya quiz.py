from tkinter import  *
from tkinter import messagebox
from tkinter import filedialog
import random 
import tkinter as tk
root = Tk()
#these make life of python


c = Canvas(root, height=600, width=600, bg="light blue")
f = Frame(root, height=300, width=300, bg="light yellow")
#this is my stuff to start the whole code or else it would be bad w / o it

root.title("anaya quiz")
root.geometry("400x500")
root.resizable(True, True)
#this is the title of the window and the size of it and if it can be resized or not


#my questions for the code :D

class memoryquizapp:
    
    def __init__(self,root): #this is a function , it has all of my question in the list
        self.root=root
    
        self.questions = [
            {"question": "what is my fav drink", "answer": "pink lemonade"},
            {"question": "whats my fav animal", "answer": "bear"},
            {"question": "what is my fav ice cream", "answer": "strawberry"},
            {"question": "what is my fav candy", "answer": "skittles"},
            {"question": "what is my fav dessert", "answer": "sundae"},
            {"question": "what is my fav food", "answer": "fries"},
            {"question": "what is my fav fruit", "answer": "strawberry"},
            {"question": "what is my fav snack", "answer": "chips"},
            {"question": "what is my fav color", "answer": "pink"},
            {"question": "what is my fav game", "answer": "roblox"},
            {"question": "what is my fav movie", "answer": "coco"},
            {"question": "what is my fav show", "answer": "family reunion"},
            {"question": "what is my fav book", "answer": "the very unfortunate wish of melony yoshimura"},
            {"question": "what is my fav song", "answer": "goddess - laufey"},
            {"question": "what is my fav place", "answer": "food court"},
            {"question": "what is my fav store", "answer": "showcase"},
            {"question": "what is my fav season", "answer": "winter"},
            {"question": "what is my fav holiday", "answer": "christmas"},
            {"question": "what is my fav sport", "answer": "volleyball"},
            {"question": "what is my fav subject", "answer": "art"},
            {"question": "what is my fav place to eat", "answer": "harvey's"},
            {"question": "what is my fav place to hang out", "answer": "mall"},
            {"question": "how do you feel about these questions (good)", "answer": "good"},
            {"question": "what is my fav hobby", "answer": "drawing"}
            
        ]
        self.score = 0 #its at 0 because , we start at 0
        self.current_question = None #theres no question yet
        self.create_widgets() #creates the widget function
        
    def show_question(self): #this randomly takes stuff from my questions, called self.questions
        self.current_question = random.choice(self.questions)
        self.question_label.config(text=self.current_question["question"]) #this makes the label become the current question it randomly chose

        
    
    def check_answer(self):
        persons_answer = self.answer_entry.get() #this gets the users answer 
        correct_answer = self.current_question["answer"] #this shows the answer
        if persons_answer.lower() == correct_answer.lower(): #this shows up if the persons code is right, it adds one and says it
            self.score += 1
            messagebox.showinfo("correct", "yyour answer is correct!1!!")
        else:
            messagebox.showerror("wrongg :(", f"correct answer is {correct_answer}") #if its not, it'll show this and not change the score
        self.score_label.config(text=f"score: {self.score} !")
        self.show_question()
    
    def create_widgets(self): #here is where all the things get on the canvas
        menu_bar = tk.Menu(self.root) #menubar
        self.root.config(menu=menu_bar) #makes menu be the nickname for menubar

        file_menu = tk.Menu(menu_bar, tearoff=0) #its the file menu
        menu_bar.add_cascade(label="file", menu=file_menu) #this adds the little label on the menu
        file_menu.add_command(label="leave hehe", command=self.root.quit) #this is an option in the file section that lets you leave

        
        self.question_label = tk.Label(self.root, text="") #this is the label it creates the question label (the thing will go inside)
        self.question_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20) #heres my geometetry thing to adjust the label size

        self.answer_label = tk.Label(self.root, text="your answerr:") #here is the label that is next to the entry box, it just is there
        self.answer_label.grid(row=1, column=0, padx=30, pady=20, sticky="e")

        self.answer_entry = tk.Entry(self.root) #entry box adjustment
        self.answer_entry.grid(row=1, column=1, padx=30, pady=20, sticky="w")

        self.check_button = tk.Button(self.root, text="check answer (wowowowoie)", command=self.check_answer) #this is my button for the check answer, i dont know how to make it enter to be correct soo D:
        self.check_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.score_label = tk.Label(self.root, text="score: 0 !") #score label
        self.score_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.show_question()


        pass

    
if __name__ == "__main__": 
    root = tk.Tk()
    app = memoryquizapp(root)
    
root.mainloop()
#the end of this very interesting projectt 1!1!1!1!!!!1!!1!1!!
