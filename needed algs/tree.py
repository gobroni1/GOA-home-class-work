import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from tkinter import ttk

class Task:
    def __init__(self, name):
        self.name = name
        self.subtasks = []

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    def display(self, level=0):
        indent = "  " * level
        return f"{indent}- {self.name}\n" + ''.join(subtask.display(level + 1) for subtask in self.subtasks)

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display(self):
        return f"Project: {self.name}\n" + ''.join(task.display() for task in self.tasks)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Project Tree Generator")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.projects = {}


        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=(10, 5))

        self.project_button = tk.Button(button_frame, text="Create Project", command=self.create_project)
        self.project_button.grid(row=0, column=0, padx=5)


        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 10))
        self.status_label.pack(pady=(5, 10))

    def create_project(self):
        project_name = simpledialog.askstring("Project Name", "Enter the project name:")
        if project_name:
            project = Project(project_name)
            self.projects[project_name] = project  
            project_frame = tk.Frame(self.notebook)
            self.notebook.add(project_frame, text=project_name)

            self.create_project_widgets(project_frame, project)
            self.status_label.config(text=f"Project '{project_name}' created successfully!", fg="black")
        else:
            self.status_label.config(text="Project name cannot be empty!", fg="red")

    def create_project_widgets(self, frame, project):
        output_text = scrolledtext.ScrolledText(frame, width=60, height=15, font=("Courier New", 10))
        output_text.pack(pady=(10, 10))

        button_frame = tk.Frame(frame)
        button_frame.pack(pady=(0, 10))

        task_button = tk.Button(button_frame, text="Add Task", command=lambda: self.add_task(project))
        task_button.grid(row=0, column=0, padx=5)

        display_button = tk.Button(button_frame, text="Display Project", command=lambda: self.display_project(project, output_text))
        display_button.grid(row=0, column=1, padx=5)

    def add_task(self, project):
        task_name = simpledialog.askstring("Task Name", "Enter the task name:")
        if task_name:
            task = Task(task_name)
            project.add_task(task)
            self.status_label.config(text=f"Task '{task_name}' added successfully!", fg="black")
            
            # Adding subtasks
            while True:
                subtask_name = simpledialog.askstring("Subtask Name", "Enter a subtask name (or leave empty to stop):")
                if not subtask_name:
                    break
                subtask = Task(subtask_name)
                task.add_subtask(subtask)
        else:
            self.status_label.config(text="Task name cannot be empty!", fg="red")

    def display_project(self, project, output_text):
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, project.display())
        self.status_label.config(text="Project displayed successfully!", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
