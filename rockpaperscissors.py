import tkinter as tk
from tkinter import messagebox
import random

# Choices and winning rules
CHOICES = ["Rock", "Paper", "Scissors"]
WIN_RULES = {
    ("Rock", "Scissors"),
    ("Scissors", "Paper"),
    ("Paper", "Rock")
}

# Game state variables
user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score
    comp_choice = random.choice(CHOICES)
    result = ""
    if user_choice == comp_choice:
        result = "Tie!"
    elif (user_choice, comp_choice) in WIN_RULES:
        user_score += 1
        result = "You win!"
    else:
        comp_score += 1
        result = "Computer wins!"

    # Update labels
    lbl_user_choice.config(text=f"You chose: {user_choice}")
    lbl_comp_choice.config(text=f"Computer chose: {comp_choice}")
    lbl_result.config(text=result)
    lbl_score.config(text=f"Score — You: {user_score}  Computer: {comp_score}")

    # Ask to play again
    if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
        # Continue – no action needed
        pass
    else:
        messagebox.showinfo("Game Over", f"Final Score — You: {user_score}  Computer: {comp_score}")
        root.destroy()

# Set up GUI
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")

tk.Label(root, text="Choose your move:", font=("Arial", 14)).pack(pady=10)

frm_buttons = tk.Frame(root)
for choice in CHOICES:
    btn = tk.Button(frm_buttons, text=choice, width=10,
                    command=lambda c=choice: play(c))
    btn.pack(side="left", padx=5)
frm_buttons.pack(pady=5)

lbl_user_choice = tk.Label(root, text="You chose: —", font=("Arial", 12))
lbl_user_choice.pack(pady=5)
lbl_comp_choice = tk.Label(root, text="Computer chose: —", font=("Arial", 12))
lbl_comp_choice.pack(pady=5)
lbl_result = tk.Label(root, text="", font=("Arial", 16, "bold"))
lbl_result.pack(pady=10)
lbl_score = tk.Label(root, text="Score — You: 0  Computer: 0", font=("Arial", 12))
lbl_score.pack(pady=5)

root.mainloop()
