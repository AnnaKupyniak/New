import tkinter as tk 
from tkinter import filedialog

class ToDoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("To do list")
        self.configure(bg='black')


        self.create_widgets()
    def create_widgets(self):
        self.task_input = tk.Entry(self, width=30, bg='#F0F8FF', fg='black')
        self.task_input.pack(pady=10)

        self.add_task_button = tk.Button(self, text="Add task", command=self.add_task, bg='#90EE90', fg='black')
        self.add_task_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(self, selectmode=tk.SINGLE, bg='#F0F8FF', fg='black')
        self.tasks_listbox.pack(pady=5)

        self.button_frame = tk.Frame(self, bg='black')
        self.button_frame.pack(pady=5)

        self.edit_task_button = tk.Button(self.button_frame, text="Edit task", command=self.edit_task, bg='#6495ED', fg='black')
        self.edit_task_button.grid(row=0, column=0, padx=5)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete task", command=self.delete_task, bg='#FFE4E1', fg='black')
        self.delete_task_button.grid(row=0, column=1, padx=5)

        self.save_button = tk.Button(self, text="Save", command=self.save_tasks, bg='#3CB371', fg='black')
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(self, text="Load", command=self.load_tasks, bg='#66CDAA', fg='black')
        self.load_button.pack(pady=5)

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks_listbox.insert(tk.END,task)
            self.task_input.delete(0,tk.END)

    def edit_task(self):
       task_index = self.tasks_listbox.curselection()
       if task_index:
           new_task = self.task_input.get()
           if new_task:
               self.tasks_listbox.delete(task_index)
               self.tasks_listbox.insert(task_index,new_task)
               self.task_input.delete(0,tk.END)


    def delete_task(self):
        task_index = self.tasks_listbox.curselection()
        if task_index:
            self.tasks_listbox.delete(task_index)

    def save_tasks(self):
        tasks = self.tasks_listbox.get(0,tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path,'w') as file:
                for task in tasks:
                    file.write(task + "\n")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path,'r') as file:
                tasks = [line.strip() for line in file.readlines()]

            self.tasks_listbox.delete(0,tk.END)

            for task in tasks:
                self.tasks_listbox.insert(tk.END,task)
    