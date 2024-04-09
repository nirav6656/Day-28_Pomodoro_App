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
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label_text.config(text="Timer")
    checkmark.config(text="")
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
        count_down(long_break_sec)
        timer_label_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label_text.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label_text.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=60, pady=60)
window.title("Pomodoro App")
window.config(background="black")

timer_label_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg="black")
timer_label_text.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=204, height=230, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102, 115, image=tomato_image)
timer_text = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 14, "bold"))
canvas.config(background="black")
canvas.grid(column=1, row=1)

# Start Button
start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

# CheckMark
checkmark = Label(text="✅", fg=GREEN, bg="black")
checkmark.grid(column=1, row=3)

# End Button
end_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0)
end_button.grid(column=2, row=3)

window.mainloop()
