from tkinter import *


# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MAIN_FONT = (FONT_NAME, 35, "bold")
BUTTON_FONT = (FONT_NAME, 10, "bold")
CHECK_FONT = (FONT_NAME, 15, "bold")

# TIMER RESET

#  TIMER MECHANISM

# COUNTDOWN MECHANISM

#  UI SETUP

window = Tk()
window.title("*** Pomodoro ***")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(window, text="Timer", font=MAIN_FONT, foreground=GREEN, bg=YELLOW)
title_label.grid(row=0, column=2)

canvas = Canvas(window, width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato = PhotoImage(file='./tomato.png')
canvas.create_image(100, 112, image=tomato)
canvas.create_text(103, 130, text="00:00", font=MAIN_FONT, fill='white')
canvas.grid(row=1, column=2)

start_button = Button(text="Start", width=10, bg=GREEN, font=BUTTON_FONT)
start_button.grid(row=2, column=1)

reset_button = Button(text="Reset", width=10, bg=PINK, font=BUTTON_FONT)
reset_button.grid(row=2, column=3)

checkmark = Label(window, text="✔️", fg=GREEN, bg=YELLOW, font=CHECK_FONT)
checkmark.grid(row=3, column=2)

window.mainloop()