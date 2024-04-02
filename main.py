from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    if count > 0:
        canvas.itemconfig(timer_text, text=str(count))
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
timer_text = canvas.create_text(103, 125, text="24.59", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=2, column=2)


button_start = Button(text="Start", bg="white", font=(FONT_NAME, 13, "bold"), highlightthickness=0)
button_start.grid(row=3, column=1)

button_reset = Button(text="Reset", bg="white", font=(FONT_NAME, 13, "bold"), highlightthickness=0)
button_reset.grid(row=3, column=3)

label_mark = Label(text="✔", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
label_mark.grid(row=4, column=2)

window.mainloop()
