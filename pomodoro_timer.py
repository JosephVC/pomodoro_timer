"""
This is a simple Pomodoro timer done in tkinter.

I'm needing something with a bit more functionality than what I've seen offered
so far.

You also have the option of setting the transparency of the app, in case you
want it to remain visible in the corner of your screen.
"""

from tkinter import *
from tkinter import ttk

# Set the root of the project
root = Tk()

# Define the widgets and their qualities
content = ttk.Frame(root, padding=(12,12, 12,12))
frame = ttk.Frame(content, borderwidth=5, relief='sunken', width=500,
height=400)
text1 = ttk.Label(content, text="Time")
time_up = ttk.Label(content, text="")
time = ttk.Entry(content)
start_button = ttk.Button(content, text="START")

# create the countdown timer
# the timer should be an entry box that allows the user to enter their time
# in turn, the time they enter should be passed below to the timer logic
# so, the time ttk.Entry above should actually be the time, with the logic
# working with whatever the user enters

remaining = 0

def countdown(time):
    if remaining is not None:
        remaining = remaining
    if remaining <= 0:
        time_up.configure(text="TIME'S UP")
    else:
        time.configure(text="{}".format(remaining))
        remaining -= 1


# Grid the widgets
# TODO -- everything is very spread out
content.grid(column=0, row=0, sticky=(N,S,E,W))
frame.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=(N,S,E,W))
text1.grid(column=1, row=0, columnspan=1)
time.grid(column=0, row=0, columnspan=1)
start_button.grid(column=0, row=1, columnspan=1)

root.mainloop()
