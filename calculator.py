import tkinter as tk
from tkinter import messagebox

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))
    display_label.config(text=current + str(number))

def clear():
    entry.delete(0, tk.END)
    display_label.config(text="")

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])
    display_label.config(text=current[:-1])

def operation_click(op):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + op)
    display_label.config(text=current + op)

def equal():
    try:
        # Perform the calculation
        equation = entry.get()
        result = eval(equation)  # Using eval to evaluate the expression
        entry.delete(0, tk.END)
        entry.insert(0, result)

        # Display the result on the label
        display_label.config(text=f"{equation} = {result}")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))
        display_label.config(text="")
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        display_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Display for input and operations (shows everything entered and result in one line)
display_label = tk.Label(root, text="", font=("Arial", 14), anchor="e", bg="white", relief="sunken", height=2)
display_label.grid(row=0, column=0, columnspan=4, sticky="we", padx=5, pady=5)

# Entry field for user input
entry = tk.Entry(root, font=("Arial", 18), borderwidth=5, justify="right", bg="lightgray")
entry.grid(row=1, column=0, columnspan=4, sticky="we", padx=5, pady=5)

# Number buttons (with blue background for numbers)
button_numbers = [
    (1, 2, 0), (2, 2, 1), (3, 2, 2),
    (4, 3, 0), (5, 3, 1), (6, 3, 2),
    (7, 4, 0), (8, 4, 1), (9, 4, 2),
    (0, 5, 1)
]

for num, row, col in button_numbers:
    tk.Button(root, text=str(num), font=("Arial", 14), width=5, height=2, bg="lightblue", command=lambda n=num: button_click(n)).grid(row=row, column=col)

# Operation buttons (with green background for operations)
operations = [("+", 2, 3), ("-", 3, 3), ("*", 4, 3), ("/", 5, 3)]
for op, row, col in operations:
    tk.Button(root, text=op, font=("Arial", 14), width=5, height=2, bg="lightgreen", command=lambda o=op: operation_click(o)).grid(row=row, column=col)

# Clear, Backspace, and Equal buttons (with customized colors)
tk.Button(root, text="C", font=("Arial", 14), width=5, height=2, bg="red", fg="white", command=clear).grid(row=5, column=0)
tk.Button(root, text="←", font=("Arial", 14), width=5, height=2, bg="yellow", command=backspace).grid(row=5, column=2)
tk.Button(root, text="=", font=("Arial", 14), width=5, height=2, bg="orange", command=equal).grid(row=5, column=3)

# Run the application
root.mainloop()
