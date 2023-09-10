from tkinter import *
# from tkinter.ttk import *

# Create the root window
root = Tk()

# root window title and dimension
root.title("Welcome to my first GUI")

# Set geometry using the width and height variables
root.geometry('300x300')

#** widgets will be here **#

#! must run mainloop() method. This is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed. if you don't put this, the window will disappear immediately.
root.mainloop()