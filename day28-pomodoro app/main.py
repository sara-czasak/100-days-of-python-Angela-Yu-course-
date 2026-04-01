from tkinter import *


# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
MAIN_FONT = (FONT_NAME, 35, "bold")
BUTTON_FONT = (FONT_NAME, 10, "bold")
CHECK_FONT = (FONT_NAME, 15, "bold")
REPS = 0

# TIMER RESET

#  TIMER MECHANISM


# COUNTDOWN MECHANISM
def count_down(count):
    minutes = int(count / 60)
    seconds = count % 60


    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# Start button function
def start_timer():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        title_label["text"] = "Break"
        count_down(LONG_BREAK_MIN * 60)
        checkmark['text'] += "✔️"
    elif REPS % 2 == 0:
        title_label["text"] = "Break"
        count_down(SHORT_BREAK_MIN * 60)
        checkmark['text'] += "✔️"
    else:
        title_label["text"] = "Work"
        count_down(WORK_MIN * 60)

def reset_timer():
    global REPS
    REPS = 0
    title_label["text"] = "Timer"
    checkmark['text'] = ""

# UI
window = Tk()
window.title("*** Pomodoro ***")
window.config(padx=10, pady=10, bg=YELLOW)


title_label = Label(window, text="Timer", font=MAIN_FONT, foreground=GREEN, bg=YELLOW)
title_label.grid(row=0, column=2)

canvas = Canvas(window, width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato = PhotoImage(file='./tomato.png')
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(103, 130, text="00:00", font=MAIN_FONT, fill='white')
canvas.grid(row=1, column=2)

start_button = Button(text="Start", width=10, bg=GREEN, font=BUTTON_FONT, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=1)

reset_button = Button(text="Reset", width=10, bg=PINK, font=BUTTON_FONT, highlightthickness=0)
reset_button.grid(row=2, column=3)

checkmark = Label(window, text="", fg=GREEN, bg=YELLOW, font=CHECK_FONT, highlightthickness=0)
checkmark.grid(row=3, column=2)

window.mainloop()