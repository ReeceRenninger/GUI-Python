from tkinter import *

# Create the root window
root = Tk()

# root window title and dimension
root.title("Welcome to my first GUI")

# Set geometry using the width and height variables
root.geometry('300x300')

#** labels **#
lbl = Label(root, text = "Are you a coder?")
lbl.grid(column = 0, row = 0) # grid() method is used to arrange labels in a table-like structure.

#** buttons **#
def clicked():
    lbl.configure(text = "You changed the label text!")

btn = Button(root, text="Click to change text", fg="red", command=clicked)

btn.grid(column=1, row=0)


#** widgets will be here **#

#! must run mainloop() method. This is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed. if you don't put this, the window will disappear immediately.
root.mainloop()