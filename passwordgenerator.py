import tkinter as tk
from tkinter import messagebox
import secrets, string

# Function to generate password
def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid positive integer for length.")
        return

    # Build character pool based on selections
    pool = ""
    if lowercase_var.get(): pool += string.ascii_lowercase
    if uppercase_var.get(): pool += string.ascii_uppercase
    if digits_var.get():    pool += string.digits
    if symbols_var.get():   pool += string.punctuation

    if not pool:
        messagebox.showwarning("No Characters", "Select at least one character set.")
        return

    # Use secrets.choice for cryptographically secure randomness
    password = ''.join(secrets.choice(pool) for _ in range(length))
    password_var.set(password)

# Function to copy password to clipboard
def copy_to_clipboard():
    pwd = password_var.get()
    if not pwd:
        messagebox.showinfo("Oops!", "Nothing to copy.")
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    messagebox.showinfo("Copied!", "Password copied to clipboard.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Strong Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Variables
length_var = tk.StringVar(value="12")
password_var = tk.StringVar()
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var    = tk.BooleanVar(value=True)
symbols_var   = tk.BooleanVar(value=True)

# Widgets
tk.Label(root, text="Password length:").pack(pady=(15,0))
tk.Entry(root, textvariable=length_var, width=5).pack()

tk.Label(root, text="Include characters:").pack(pady=(10,0))
tk.Checkbutton(root, text="Lowercase (a–z)", variable=lowercase_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Uppercase (A–Z)", variable=uppercase_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Digits (0–9)", variable=digits_var).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Symbols (!@#$...)", variable=symbols_var).pack(anchor="w", padx=20)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=15)
tk.Entry(root, textvariable=password_var, width=30, state="readonly", justify="center").pack(pady=(0,10))
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

root.mainloop()
