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
_input = ttk.Entry(master=window)
_input.pack()

# button
_button = ttk.Button(master=window, text="Greet")
_button.pack()

# run the loop
window.mainloop()
