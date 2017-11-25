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
root.title("Pomodoro Timer")

# state variables

entered_time = StringVar()
statusmsg = StringVar()
remaining = 0

# create the countdown timer
# if a number is entered in the time box and the user hits the start_button,
# then the timer should visibly count down
# the timer should be an entry box that allows the user to enter their time
# in turn, the time they enter should be passed below to the timer logic
# so, the time ttk.Entry above should actually be the time, with the logic
# working with whatever the user enters
def countdown():
    # if time field has content
    # if start_button has been pressed
    # display time time running down

    if time is not None:
        if remaining is not None:
            remaining = remaining
        if remaining <= 0:
            statusmsg.configure(text="TIME'S UP")
        else:
            statusmsg.configure(text="{}".format(remaining))
            remaining -= 1

# Define the widgets and their qualities
content = ttk.Frame(root, padding=(3,3, 12,12))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=500,
height=400)
text1 = ttk.Label(content, text="Time", width=4)
#time_up = ttk.Label(content, text="Time Up")
#  QUESTION: HOW DO I PASS USER INPUT TO AN ENTRY BOX
#  ANSWER: make the text entry box a ttk.Entry box attached to a textvariable

time = ttk.Entry(content, width=7, textvariable=entered_time)
start_button = ttk.Button(content, text="START", command=countdown)
stop_button = ttk.Button(content, text="STOP")
status = ttk.Label(content, textvariable = statusmsg, anchor= W )


# Grid the widgets
# TODO -- everything is very spread out, better structure grid
content.grid(column=0, row=0, sticky=(N,S,E,W))
#content.columnconfigure(3, weight=5)
frame.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=(N,S,E,W))
text1.grid(column=1, row=0, columnspan=1)
time.grid(column=0, row=0, columnspan=1)
start_button.grid(column=0, row=1, columnspan=1)
stop_button.grid(column=0, row=2, columnspan=1)
status.grid(column=1, row=3, columnspan=1)

# set event bindings
start_button.bind('<Double-1>', countdown)
# stop_button.bind(pause the countdown )

# run mainloop
root.mainloop()
