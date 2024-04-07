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

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=60,pady=60)
window.title("Pomodoro App")
window.config(background="black")

timer_text = Label(text="Timer",fg=GREEN, font=(FONT_NAME,20,"bold"),bg="black")
timer_text.grid(column=1,row=0)

# Canvas
canvas = Canvas(width=204, height=230, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102,115,image=tomato_image)
canvas.create_text(102,130,text="00:00",font=(FONT_NAME,14,"bold"))
canvas.config(background="black")
canvas.grid(column= 1,row=1)

# Start Button
start_button = Button(text="Start",width=10,font=(FONT_NAME,6,"bold"))
start_button.grid(column=0,row=3)

# CheckMark
checkmark = Label(text="✅",fg=GREEN,bg="black")
checkmark.grid(column=1,row=3)

# End Button
end_button = Button(text="Reset",width=10,font=(FONT_NAME,6,"bold"))
end_button.grid(column=2,row=3)


window.mainloop()