import Tkinter as tk
from Tkinter import *
import time

# define break and wait timings in seconds
BREAK_TIME = 20
WAIT_TIME = 1200

BREAK_TIME_TEST = 5
WAIT_TIME_TEST = 10

# dialog constants
break_dialog_title = "Break Time.."


def countdown(count, label, root):
    """
    Countdown for given seconds
    :param count: counter for break
    :param label: label for window
    :param root: Tk root
    """
    label['text'] = " Take a break for : " + str(count) + " sec"

    if count > 0:
        root.after(1000, countdown, count - 1, label, root)
    else:
        root.destroy()


def show_break_dialog():
    """
    Show break dialog with message
    """
    root = tk.Tk()
    root.lift()
    root.attributes('-topmost', True)
    root.resizable(0, 0)

    root.title(break_dialog_title)
    label = tk.Label(root, font=("Helvetica", 16), pady=25)
    label.pack()
    Button(root, text="CANCEL", font=("Helvetica", 16), command=root.destroy).pack()

    countdown(BREAK_TIME, label, root)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("350x150+%d+%d" % (screen_width / 2 - 275, screen_height / 2 - 125))

    root.mainloop()


if __name__ == '__main__':
    while True:
        # show take break dialog
        show_break_dialog()
        # wait for 20 minutes
        time.sleep(WAIT_TIME)
