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

# run the loop
window.mainloop()
