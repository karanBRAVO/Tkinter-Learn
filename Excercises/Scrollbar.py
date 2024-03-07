# Frame Scrollbar (using Canvas Widget)

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Scrollbar")
root.geometry("500x400")

main_frame = tk.Frame(root,
                      background="#000000")
main_frame.pack(fill=tk.BOTH,
                expand=True)

canvas = tk.Canvas(main_frame,
                   background="#ffff00")
canvas.pack(side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx=15,
            pady=15)

scrollbar = ttk.Scrollbar(main_frame,
                          orient=tk.VERTICAL,
                          command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

frame_buttons = ttk.Frame(canvas)
canvas.create_window((0, 0),
                     window=frame_buttons,
                     anchor='nw')

for i in range(100):
    ttk.Button(frame_buttons,
               text=f"Button {i+1}").grid(row=i,
                                          column=0,
                                          padx=10,
                                          pady=10)

frame_buttons.update_idletasks()  # Update to get correct frame size

canvas.config(scrollregion=canvas.bbox("all"))

canvas.bind('<Configure>',
            lambda e: canvas.config(
                scrollregion=canvas.bbox("all")))

root.mainloop()
