import tkinter as tk
import random
from tkinter import messagebox

# Function to determine the winner
def play(choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer = random.choice(options)
    result = ""

    if choice == computer:
        result = f"Both chose {choice}.\nIt's a Tie!"
    elif (choice == "Rock" and computer == "Scissors") or \
         (choice == "Paper" and computer == "Rock") or \
         (choice == "Scissors" and computer == "Paper"):
        result = f"You chose {choice}, computer chose {computer}.\nYou Win!"
    else:
        result = f"You chose {choice}, computer chose {computer}.\nYou Lose!"

    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("360x250")

# Heading
title_label = tk.Label(root, text="Make your choice", font=("Arial", 16))
title_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Buttons
rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
exit_btn = tk.Button(root, text="Exit", width=10, command=root.quit)

# Arrange buttons in the frame
rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)
exit_btn.pack(pady=10)

# Start the GUI loop
root.mainloop()