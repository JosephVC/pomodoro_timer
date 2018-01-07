"""
This is a simple Pomodoro timer done in tkinter.

I'm needing something with a bit more functionality than what I've seen offered
so far.

You also have the option of setting the transparency of the app, in case you
want it to remain visible in the corner of your screen.
"""
from tkinter import *
from tkinter import ttk
import threading
import time

# create the basic elements
root = Tk()
root.title("Pomodoro Timer")

entry_box = Entry(root)
entry_box.pack()

# this is how I ensure what is entered for an argument in the countdown function
# is an integer that can be worked with


display_box = ttk.Label(root, text="I'm a display box!")
display_box.pack()

# create a countdown functionality
def countdown():
    def _inner():
        countdown_from = int(entry_box.get())
        while countdown_from > 0:
            display_box.configure(text=countdown_from)
            time.sleep(1)
            countdown_from -= 1
            if countdown_from <= 0:
                display_box.configure(text="done")
    thread = threading.Thread(target=_inner)
    thread.start()

countdown_button = ttk.Button(root, text="countdown", command=countdown)
countdown_button.pack()

# run the program
root.mainloop()
