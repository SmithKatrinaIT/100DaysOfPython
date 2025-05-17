"""
    Concept: Creating GUIs using Tkinter to read and react to our Python code
    -- tkinter.Tk(): creates a window
    -- window.mainloop(): creates the window on the screen until some other condition is met
    -- Must first create components to show on the screen using various Tkinter Classes
    -- 3 Primary ways to place objects on the screen (GUI)
        -- pack(): A Packer `.pack() method` will place the component on the screen and automatically center it when called on the component
            -- if no other specifications are configured
        -- place(): uses X,Y coordinates to place objects precisely where intended
        -- grid(): divide program into columns and rows.
        NOTE: can't use grid() and pack() in the same program
    -- Import all Tkinter class using the following syntax.  Save on typing
        -- from tkinter import *

    -- Link to Tkinter Documentation: https://www.tcl-lang.org/man/tcl8.6/contents.htm

"""

#import tkinter
from tkinter import *

KILOMETER = 1.609344

def convert_miles_to_km():
    miles = float(miles_input.get())
    km = miles * KILOMETER
    value_label.config(text=f"{km}")

#window = tkinter.Tk()
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=100)
window.config(padx=20, pady=20)

""" Creating components to go into the screen or GUI """
#Entry component (acts as in input field)
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

#Label Component
miles_label = Label(text="Miles", font=("Courier", 18, "bold"))
miles_label.config(padx=20, pady=0)
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to", font=("Courier", 18, "bold"))
equal_to_label.grid(column=0, row=1)

value_label = Label(text="0", font=("Courier", 18, "normal"))
value_label.grid(column=1, row=1)
value_label.config(padx=4, pady=10)

kilo_label = Label(text="Km", font=("Courier", 18, "bold"))
kilo_label.grid(column=2, row=1)


#button component = tkinter.Button(text="Click Me", command=button_clicked)
calculate = Button(text="Calculate", command=convert_miles_to_km) #command key acts as an event lister for the button
calculate.grid(column=1, row=2)




# keeps the window open
window.mainloop()