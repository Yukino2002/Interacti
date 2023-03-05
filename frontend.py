import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

from draganddrop import drag_and_drop
from zoom import virtual_zoom
from writing import real_time_writing


def drag_and_drop_click():
    drag_and_drop()
    print("you clicked")


def zoom_click():
    filename = askopenfilename()
    virtual_zoom(filename)
    print("you clicked")


def real_time_writing_click():
    real_time_writing()
    print("you clicked")


window = tk.Tk()

window.title("Welcome to OpenClassroom")
ttk.Label(window, text="Hello, OpenClassroom! Choose one of the modes below").pack()
ttk.Button(window, text="Drag and Drop", command=drag_and_drop_click).pack()
ttk.Button(window, text="Zoom", command=zoom_click).pack()
ttk.Button(window, text="Real Time Writing", command=real_time_writing_click).pack()
window.mainloop()
