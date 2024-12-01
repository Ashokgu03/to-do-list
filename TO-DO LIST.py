import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def complete_task():
    try:
        task_index = listbox.curselection()[0]
        task = listbox.get(task_index)
        listbox.delete(task_index)
        listbox.insert(tk.END, f"[x] {task}") #Mark as complete
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")


# Create main window
window = tk.Tk()
window.title("To-Do List")

# Entry field
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Add button
add_button = tk.Button(window, text="Add Task", width=20, command=add_task)
add_button.pack()

# Listbox to display tasks
listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)

# Delete button
delete_button = tk.Button(window, text="Delete Task", width=20, command=delete_task)
delete_button.pack()

# Complete button
complete_button = tk.Button(window, text="Complete Task", width=20, command=complete_task)
complete_button.pack()


window.mainloop()