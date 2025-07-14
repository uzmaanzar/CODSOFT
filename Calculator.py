# gui_calculator.py
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Error: Division by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI Setup
app = tk.Tk()
app.title("Simple Calculator")
app.geometry("300x250")

# Input Fields
tk.Label(app, text="Enter first number:").pack()
entry1 = tk.Entry(app)
entry1.pack()

tk.Label(app, text="Enter second number:").pack()
entry2 = tk.Entry(app)
entry2.pack()

# Operation Options
tk.Label(app, text="Choose operation:").pack()
operator = tk.StringVar(app)
operator.set('+')  # default value
tk.OptionMenu(app, operator, '+', '-', '*', '/').pack()

# Calculate Button
tk.Button(app, text="Calculate", command=calculate).pack(pady=10)

# Result Label
result_label = tk.Label(app, text="Result:")
result_label.pack()

# Run GUI
app.mainloop()
