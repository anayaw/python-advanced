'''
To-Do List App
Author: anayaa
Date: mar 6, 2025

a like todo list
'''


from tkinter import *
from tkinter import ttk

root = Tk()
root.title("TODO List App")
root.geometry("400x500")  
root.resizable(True, True) 


class ProgressBar:
    def __init__(self, parent):
        self.progress_var = DoubleVar()
        self.progress_bar = ttk.Progressbar(parent, variable=self.progress_var, mode='determinate')
        self.progress_bar.pack(fill=X, padx=10, pady=5)

    def update_progress(self, total, completed):
        if total > 0:
            self.progress_var.set((completed / total) * 100)
        else:
            self.progress_var.set(0)


class ListItem:
    def __init__(self, parent, text, app):
        self.parent = parent
        self.app = app
        self.var = IntVar()

        self.frame = Frame(parent, bg="lightblue", padx=5, pady=5)
        self.frame.pack(fill=X, pady=2)

        self.checkbox = Checkbutton(self.frame, text=text, variable=self.var, command=self.update_progress)
        self.checkbox.pack(side=LEFT, padx=5)

        self.delete_button = Button(self.frame, text="🗑", command=self.delete_item)  
        self.delete_button.pack(side=RIGHT)

    def update_progress(self):
        self.app.update_progress()

    def delete_item(self):
        self.frame.destroy()
        self.app.items.remove(self)
        self.app.update_progress()


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.items = []  

        Label(root, text="to-do list").pack(pady=5)

        self.progress_bar = ProgressBar(root)

        Label(root, text="enter a task:").pack(pady=2)

        self.entry = Entry(root)
        self.entry.pack(fill=X, padx=10, pady=5)
        self.entry.bind("<Return>", self.add_item)

        self.todo_frame = Frame(root)
        self.todo_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

    def add_item(self, event=None):
        text = self.entry.get().strip()
        if text:
            item = ListItem(self.todo_frame, text, self)
            self.items.append(item)  
            self.entry.delete(0, END)
            self.update_progress()

    def update_progress(self):
        total = len(self.items)
        completed = sum(item.var.get() for item in self.items)
        self.progress_bar.update_progress(total, completed)


app = ToDoApp(root)
root.mainloop()
