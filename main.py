from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
LYELLOW = "lightyellow"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_reset = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps
    reps = 0
    window.after_cancel(timer_reset)
    label1.config(text="Timer", fg="green")
    canvas.itemconfig(text_count, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1

    if reps % 8 == 0:
        countdown(work_sec)
        # countdown(LONG_BREAK_MIN)
        label1.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break)
        # countdown(SHORT_BREAK_MIN)
        label1.config(text="Break", fg=PINK)
    else:
        countdown(long_break)
        # countdown(WORK_MIN)
        label1.config(text="WORK", fg="blue")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        if count_sec < 10:
            count_min = f"0{count_min}"
            count_sec = f"0{count_sec}"
            # canvas.itemconfig(text_count, text=f"0{count_min}:0{count_sec}")
        else:
            count_min = f"0{count_min}"
            # canvas.itemconfig(text_count, text=f"0{count_min}:{count_sec}")
    else:
        if count_sec < 10:
            count_sec = f"0{count_sec}"
    canvas.itemconfig(text_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_reset
        timer_reset = window.after(1000, countdown, count - 1)
    else:
        start()
        if reps > 1 and reps % 2 == 0:
            ticks = tick * (math.floor(reps / 2))
            label2.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
title = window.title("Timer")
window.config(padx=100, pady=50, bg=LYELLOW)
canvas = Canvas(width=200, height=240, bg=LYELLOW, highlightthickness=0)
tick = "✔"
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 120, image=img)
text_count = canvas.create_text(100, 140, text="00:00", font=(FONT_NAME, 33, "bold"))
canvas.grid(row=2, column=2)

label1 = Label(text="Timer", font=("Courier", 40, "bold"), bg=LYELLOW, fg="green")
label1.grid(row=1, column=2)

label2 = Label(bg=LYELLOW, fg=GREEN, font=10)
label2.grid(row=4, column=2)

start_button = Button(text="Start", highlightthickness=0, command=start)
start_button.grid(row=3, column=1)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(row=3, column=3)

window.mainloop()
