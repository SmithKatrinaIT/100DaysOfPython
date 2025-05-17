"""
    Concept: Creating GUIs using Tkinter to read and react to our Python code
    -- Grids: specify object placement using columns and rows
    -- Add Padding:
        -- To add padding around the entire program: window.config(padx=num, pady=num)
        -- To add padding around a specific element/widget: elementVar.config(padx=num, pady=num)


"""

#import tkinter
from tkinter import *

#window = tkinter.Tk()
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


""" Creating components to go into the screen or GUI """
#Label Component
#my_label = tkinter.Label(text="Im a label", font=("Courier", 24, "bold"))
my_label = Label(text="I'm a Label", font=("Courier", 24, "bold"))

# display the label on the screen.  Use grid to specify column and row
my_label.grid(column=0, row=0)


def button_clicked():
    #print("I got clicked")
    text = input.get()
    my_label.config(text=text)

#button component = tkinter.Button(text="Click Me", command=button_clicked)
button1 = Button(text="Click Me", command=button_clicked) #command key acts as an event lister for the button
button1.grid(column=1, row=1)

button2 = Button(text="Save") #command key acts as an event lister for the button
button2.grid(column=2, row=0)

#Entry component (acts as in input field)
input = Entry(width=10)
input.grid(column=3, row=2)


# keeps the window open
window.mainloop()