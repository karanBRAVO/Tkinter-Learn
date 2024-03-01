import tkinter as tk
from tkinter import ttk

# create the window
window = tk.Tk("Screen name", "Base name")

WINDOW_WIDTH = 480
WINDOW_HEIGHT = 450

# set the window title
window.title("Tkinter Basics")

# set the width and height of the window
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# set the minimum size of the window
window.minsize(WINDOW_WIDTH, WINDOW_HEIGHT)

# widgets
# label
_label = tk.Label(master=window, text="Hello World!")
_label.pack()

# input
_input_variable = tk.StringVar(master=window, value="karan yadav")
_input = ttk.Entry(master=window, textvariable=_input_variable)
_input.pack()


def greet_user():
    val = _input_variable.get()
    if not val:
        val = "Please enter your name"
    else:
        val = f"Hello, {val}"
    _label2_variable.set(val)


# button
_button = ttk.Button(master=window, text="Greet", command=greet_user)
_button.pack()

# label2
_label2_variable = tk.StringVar(master=window, value="")
_label2 = ttk.Label(master=window,
                    textvariable=_label2_variable)
_label2.pack()

# run the loop
window.mainloop()
