import random
from functions import *

print("*** WELCOME TO THE NUMBER GUESSING GAME ***")


game = True

while game:
    number = random.randint(1, 100)
    lives = set_difficulty(int(input("Choose a difficulty (1 for easy, 2 for hard): ")))
    print("I'm thinking of a number between 1 and 100")
    print(f"You have {lives} lives.")
    while lives > 0:
        guess = int(input("What's your guess? "))
        lives = check_guess(guess, number, lives)
        if guess == number:
            lives = 0
    print(f"*** GAME OVER ***\n* The number was: {number}")
    again = input("Do you want to play again? (y/n): ").lower()
    if again == "y":
        game = True
    else:
        game = False

print("*** SEE YOU NEXT TIME! ***")




