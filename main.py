import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 3
reps = 1


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_rep = [1, 3, 5, 7]
    short_break_rep = [2, 4, 6]

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in work_rep:
        count_down(work_sec)
    elif reps in short_break_rep:
        count_down(short_break_sec)
    elif reps == 1:
        count_down(long_break_sec)


def restart_timer():
    count_down(0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count == 0:
        reps += 1

        if reps == 9:
            reps = 1

        start_timer()

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count >= 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)

label_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW)
label_timer.grid(row=1, column=2)

canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 100, image=tomato)
timer_text = canvas.create_text(103, 125, text="10", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=2, column=2)

button_start = Button(text="Start", bg="white", font=(FONT_NAME, 13, "bold"), highlightthickness=0,
                      command=start_timer)
button_start.grid(row=3, column=1)

button_reset = Button(text="Reset", bg="white", font=(FONT_NAME, 13, "bold"), highlightthickness=0)
button_reset.grid(row=3, column=3)

label_mark = Label(text="✔", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
label_mark.grid(row=4, column=2)

window.mainloop()
