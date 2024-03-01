import tkinter as tk
from tkinter import ttk

# window set-up
WINDOW = tk.Tk()
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 450
WINDOW.title("Convertor")
WINDOW.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# label
ttk.Label(master=WINDOW, text="Decimal to Binary Convertor", font="10").pack()
ttk.Label(master=WINDOW, text="Decimal Number").pack()

# input field
_input_var = tk.IntVar(master=WINDOW, value=1)
_input_ = ttk.Entry(master=WINDOW, textvariable=_input_var)
_input_.pack()


def calc():
    num = _input_var.get()
    b_num = bin(num)
    _res.set(b_num[2:].rjust(64, "0"))


# button
_btn = ttk.Button(master=WINDOW, text="Convert", command=calc)
_btn.pack()

# result
_res = tk.StringVar(master=WINDOW, value="")
ttk.Label(master=WINDOW,
          textvariable=_res).pack()

WINDOW.mainloop()
