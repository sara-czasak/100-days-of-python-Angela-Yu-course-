import random


def get_quote():
    with open('quotes.txt', 'r') as f:
        quotes = f.readlines()
        quotes =[i.strip() for i in quotes]
    return random.choice(quotes)

