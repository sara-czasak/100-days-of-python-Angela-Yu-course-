from email.mime import image
from tkinter import *
from brain import *
import random


# Button functions
def new_card():
    new_card_front = random.choice(flashcard_front)
    new_card_index = flashcard_front.index(new_card_front)
    new_card_back = flashcard_back[new_card_index]
    card.itemconfig(card_text_content, text=new_card_front, fill='black')
    card.itemconfig(bg_img, image=front_img)
    card.itemconfig(card_text_title, text="QUESTION", fill='black')
    window.after(3000,flip_card, new_card_back)


def flip_card(new_card_back):
    card.itemconfig(bg_img, image=back_img)
    card.itemconfig(card_text_title, text="ANSWER", fill='white')
    card.itemconfig(card_text_content, text=new_card_back, fill='white')


# CONSTANTS
TITLE_FONT = ("Courier", 25, "bold")
CONTENT_FONT = ("Arial", 15, "italic")


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
bg_img = card.create_image(325, 210, image=front_img)
card_text_title = card.create_text(325, 70, text="", font=TITLE_FONT)
card_text_content = card.create_text(325, 210, text='', font=CONTENT_FONT)
card.grid(row=0, column=0, columnspan=2)
new_card()


# Buttons
right_button = Button(image=right_img, highlightthickness=0, command=new_card)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=1)




window.mainloop()