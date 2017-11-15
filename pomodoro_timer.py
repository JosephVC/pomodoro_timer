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
time = ttk.Entry(content)
start = ttk.Button(content, )

# create the countdown timer


# Grid the widgets
content.grid(column=0, row=0, sticky=(N,S,E,W))
frame.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=(N,S,E,W))
text1.grid(column=1, row=0, columnspan=1)
time.grid(column=0, row=0, columnspan=1)

root.mainloop()
