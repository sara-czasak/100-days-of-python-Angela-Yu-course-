from tkinter import *
from brain import *


# CONSTANTS
TITLE_FONT = ("Courier", 25, "bold")
CONTENT_FONT = ("Arial", 25, "italic")


# Data for flashcards
flashcard_front, flashcard_back = get_data()


# UI
window = Tk()
window.title("Python Concept Flashcards")
window.config(padx=50, pady=50, bg="#b1ddc6")

# Load in images
back_img = PhotoImage(file="resources/card_back.png")
front_img = PhotoImage(file="resources/card_front.png")
wrong_img = PhotoImage(file="resources/wrong.png")
right_img = PhotoImage(file="resources/right.png")

# Setup initial card
card = Canvas(window, width=650, height=420, bg='#b1ddc6', highlightthickness=0)
card.create_image(325, 210, image=front_img)
card.create_text(325, 70, text="QUESTION", font=TITLE_FONT, fill="green")
card.create_text(325, 210, text=flashcard_front[0], font=CONTENT_FONT, fill="green")
card.grid(row=0, column=0, columnspan=2)


# Buttons
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=1)




window.mainloop()