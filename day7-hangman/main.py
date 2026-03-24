import random
from words_to_guess import *

print("*** WELCOME TO HANGMAN ***")

# Generating random fraze for player to guess
fraze = random.choice(frazes)
# blanks screen
blank = ""

# Generating string with _ for each letter of chosen random fraze
for i in range(len(fraze)):
    if fraze[i] == " ":
        blank += " "
    else:
        blank += "_"

# Setting up lives
lives = 10

# Game loop
play = True

while play:
    print(blank)
    guess = input("Guess a letter: ")
    for index, i in enumerate(fraze):
        if i.lower() == guess.lower():
            blank = blank[:index] + guess + blank[index + 1:]
            if "_" not in blank:
                print("*** YOU WIN ***")

