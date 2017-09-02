import Tkinter as tk
from Tkinter import *
import time


def countdown(count, label, root):
    label['text'] = " Take a break for : " + str(count) + " sec"

    if count > 0:
        root.after(1000, countdown, count - 1, label, root)
    else:
        root.destroy()


def start():
    root = tk.Tk()

    root.lift()
    root.resizable(0, 0)

    root.title("Message...!!")
    label = tk.Label(root, font=("Helvetica", 16), pady=25)
    label.pack()
    Button(root, text="CANCEL", font=("Helvetica", 16), command=root.destroy).pack()

    countdown(20, label, root)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("350x150+%d+%d" % (screen_width / 2 - 275, screen_height / 2 - 125))

    root.mainloop()


while True:
    start()
    time.sleep(1200)
