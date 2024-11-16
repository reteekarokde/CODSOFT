import tkinter as tk
from tkinter import messagebox

# Functionality
def add_task():
    task = task_entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Do you want to clear all tasks?"):
        tasks_listbox.delete(0, tk.END)

def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Colorful To-Do List")
root.geometry("400x450")
root.config(bg="#f5f5f5")

# Styling
button_style = {"bg": "#ffde59", "fg": "black", "font": ("Arial", 12, "bold"), "width": 12}
label_style = {"bg": "#f5f5f5", "fg": "#333333", "font": ("Arial", 14, "bold")}
entry_style = {"bg": "#ffffff", "font": ("Arial", 12), "width": 30}
listbox_style = {"bg": "#fffacd", "font": ("Arial", 12), "width": 40, "height": 15}

# Widgets
task_label = tk.Label(root, text="Enter a Task:", **label_style)
task_label.pack(pady=10)

task_entry = tk.Entry(root, **entry_style)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task, **button_style)
add_button.pack(pady=5)

tasks_listbox = tk.Listbox(root, **listbox_style)
tasks_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, **button_style)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear Tasks", command=clear_tasks, **button_style)
clear_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app, bg="#ff4c4c", fg="white", font=("Arial", 12, "bold"), width=12)
exit_button.pack(pady=20)

# Run the app
root.mainloop()
