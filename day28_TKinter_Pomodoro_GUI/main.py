"""
     Concept: Creating GUIs using Tkinter to read and react to our Python code
     -- Canvas: used to insert images on/in the window object
     -- create_images requires the x,y values and a PhotoImage class object.
        -- to center the image within the canvas, x and y are specified as half the width and height of the canvas
        -- to pass an image to the canvas, use the PhotoImage class to specify the path of the image, use that variable reference in the
        create_image()
"""

from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✅"
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    checkmark_label.config(text="")

    # NOTE: canvas.itemconfig() takes in the "item" to change/configure as the first parameter
    canvas.itemconfig(timer_text, text="00:00")

    # RESET REPS
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # IF it's the 8th rep
        timer_count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # IF its the 2nd/4th/6th rep
        timer_count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        # IF it's the 1st/3rd/5th/7th rep
        timer_count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def timer_count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, timer_count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECKMARK

        checkmark_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

# WINDOW SETUP
window = Tk()
window.title("Poonodoro")
window.config(padx=150, pady=125, bg=YELLOW)

# CANVAS SETUP
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# BUTTON SETUP
start_btn = Button(text="Start", command=start_timer )
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

# LABEL(S) SETUP
timer_label = Label(text="Timer", font=(FONT_NAME, 52), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# CHECKMARK SETUP
checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=4)

window.mainloop()
