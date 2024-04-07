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
# window.config(background="black")


# Canvas
canvas = Canvas(width=204, height=230)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(102,115,image=tomato_image)
canvas.config(background="black")
canvas.pack()



window.mainloop()