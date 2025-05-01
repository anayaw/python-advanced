from tkinter import  *
from tkinter import messagebox
from tkinter import filedialog
root = Tk()
#these make life of python


c = Canvas(root, height=600, width=600, bg="light blue")
f = Frame(root, height=300, width=300, bg="light yellow")
#this is my stuff to start the whole code or else it would be bad w / o it



class memoryquizapp:
    
    def __init__(self,root):
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
            {"question": "what is my fav hobby", "answer": "drawing"}
            
        ]
        self.score = 0
        self.current_question = None
        self.create_widgets()
        
    def show_question(self):
        if self.questions:
            self.current_question = self.questions.pop(0)
            question_text = self.current_question["question"]
            self.question_label.config(text=question_text)
            self.answer_entry.delete(0, END)

        
        pass
    
    def check_answer(self):
        pass
    
    def create_widgets(self):
        pass
    
root.mainloop()
#the end of this very interesting projectt 1!1!1!1!!!!1!!1!1!!