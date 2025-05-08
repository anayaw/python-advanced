from tkinter import  *
from tkinter import messagebox
from tkinter import filedialog
import random 
import tkinter as tk

root = Tk()
# this opens the main window of the program

c = Canvas(root, height=600, width=600, bg="light blue")
f = Frame(root, height=300, width=300, bg="light yellow")
# this makes a canvas and a frame to use later if needed (not used in this version but it's okay)

root.title("anaya quiz")
root.geometry("400x500")
root.resizable(True, True)
# this sets the title, window size, and lets the window be resized


# my questions for the code :D

class memoryquizapp:
    
    def __init__(self, root): 
        # this is the function that starts when the quiz is made
        # it stores the questions and sets everything up
        self.root = root

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
        self.score = 0 
        # score starts at 0

        self.current_question = None 
        # there's no question shown yet

        self.create_widgets() 
        # this calls the function to make all the buttons and labels

    
    def show_question(self): 
        # this picks a random question from the list and shows it
        self.current_question = random.choice(self.questions)
        self.question_label.config(text=self.current_question["question"])

    
    def check_answer(self):
        # this checks if the user's answer is correct
        persons_answer = self.answer_entry.get()
        correct_answer = self.current_question["answer"]
        if persons_answer.lower() == correct_answer.lower():
            self.score += 1
            messagebox.showinfo("correct", "yyour answer is correct!1!!")
        else:
            messagebox.showerror("wrongg :(", f"correct answer is {correct_answer}")
        self.score_label.config(text=f"score: {self.score} !")
        self.show_question()

    
    def create_widgets(self):
        # this makes the labels, buttons, and menu bar
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="file", menu=file_menu)
        file_menu.add_command(label="leave hehe", command=self.root.quit)

        self.question_label = tk.Label(self.root, text="")
        self.question_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        self.answer_label = tk.Label(self.root, text="your answerr:")
        self.answer_label.grid(row=1, column=0, padx=30, pady=20, sticky="e")

        self.answer_entry = tk.Entry(self.root)
        self.answer_entry.grid(row=1, column=1, padx=30, pady=20, sticky="w")

        self.check_button = tk.Button(self.root, text="check answer (wowowowoie)", command=self.check_answer)
        self.check_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.score_label = tk.Label(self.root, text="score: 0 !")
        self.score_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.show_question()
        # show the first question when it starts

        pass

    
if __name__ == "__main__": 
    # this part starts the app if the file is run
    root = tk.Tk()
    app = memoryquizapp(root)

root.mainloop()
# keeps the window open until the user closes it
