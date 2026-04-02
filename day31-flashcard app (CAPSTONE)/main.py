from tkinter import *
from brain import *


# CONSTANTS
TITLE_FONT = ("Courier", 40, "bold")
CONTENT_FONT = ("Arial", 40, "italic")


# Data for flashcards
flashcard_front, flashcard_back = get_data()


# UI
window = Tk()
window.title("Python Concept Flashcards")

# Load in images
back_img = PhotoImage(file="resources/card_back.png")
front_img = PhotoImage(file="resources/card_front.png")
wrong_img = PhotoImage(file="resources/wrong.png")
right_img = PhotoImage(file="resources/right.png")

# Setup initial card
card = Canvas(window, width=900, height=600, bg='GREEN')
card.create_image(450, 300, image=front_img)
card.create_text(450, 70, text="QUESTION", font=TITLE_FONT, fill="green")
card.create_text(450, 300, text=flashcard_front[0], font=CONTENT_FONT, fill="green")
card.grid(row=0, column=0, padx=10, pady=10)







window.mainloop()