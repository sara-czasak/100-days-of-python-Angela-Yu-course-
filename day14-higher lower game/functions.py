import random
from game_data import *


def start_game(start):
    decision = False
    while not decision:
        if start == "y":
            decision = True
            return True
        elif start == "n":
            decision = True
            return False
        else:
            decision = False
        print("I'm sorry, I didn't catch that.")
        start = input("Are you ready to start? (y/n): ").lower()


def choose_item():
    book = random.choice(data)
    return book


def check_if_item_unique(book1, book2):
    if book1 == book2:
        return False
    else:
        return True


def check_higher(book1, book2):
    if book1['word_count'] > book2['word_count']:
        book = book1
        return book
    else:
        book = book2
        return book


def check_choice(book, choice):
    if book == choice:
        return True
    else:
        return False


def choose_next_item(book1, book2):
    if book1['word_count'] > book2['word_count']:
        book1 = book2
        book2 = choose_item()
        return book1, book2
    else:
        book1 = book1
        book2 = choose_item()
        return book1, book2

