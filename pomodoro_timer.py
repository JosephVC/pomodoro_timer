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


# Define the widgets and, for now, pack them in to the display

time = ttk.Entry(root).pack()
start_button = Entry(root).pack()
status = ttk.Label(root).pack()

# Grid the widgets
# TODO -- everything is .pack()-d in, per the above.
#         This works well enough for now, but as the app expands, widgets will
#         need to be well-gridded.


# create the countdown timer
# if a number is entered in the time box and the user hits the start_button,
# then the timer should visibly count down
# the timer should be an entry box that allows the user to enter their time
# in turn, the time they enter should be passed below to the timer logic
# so, the time ttk.Entry above should actually be the time, with the logic
# working with whatever the user enters
def countdown():
    def _inner():
        countdown_from = int(time.get())
        while countdown_from > 0:
            status.configure(text=countdown_from)
            time.sleep(1)
            countdown_from -= 1
            if countdown_from <= 0:
                display_box.configure(text="Time's Up.")
    thread = threading.Thread(target=_inner)
    thread.start()

countdown_button = Button(root, text="countdown", command=countdown).pack()

# run mainloop
root.mainloop()
