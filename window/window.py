import tkinter as tk

window = None

def create():
    global window
    window = tk.Tk()
    window.title("window")
    return window

def size(x, y):
    if window is None:
        raise RuntimeError("Window not created. Call create() first.")
    window.geometry(f"{x}x{y}")

def set_title(text):
    if window is None:
        raise RuntimeError("Window not created. Call create() first.")
    window.title(str(text))

def run():
    if window is None:
        raise RuntimeError("Window not created. Call create() first.")
    window.mainloop()
