import tkinter as tk

# Function to update the expression in the entry box
def enter(num):
    entry_text.set(entry_text.get() + str(num))

# Function to evaluate the final expressions
def equalenter():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except:
        entry_text.set("Error!!")

# Function to clear the entry box
def clear():
    entry_text.set("")

# GUI Window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x460")
root.resizable(False, False)

# Heading label
label = tk.Label(root, text="Calculator", font=("Arial", 18, "bold"))
label.pack(pady=10)

# Entry field for input and output
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 18), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right')
entry.pack(pady=10)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Creating buttons using loop
for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack(side=tk.TOP)
    for char in row:
        action = lambda x=char: enter(x) if x not in ['=', 'C'] else (equalenter() if x == '=' else clear())
        tk.Button(row_frame, text=char, padx=20, pady=20, font=('Arial', 14), command=action).pack(side=tk.LEFT, padx=5, pady=5)

# Run the GUI loop
root.mainloop()