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

# Making empty list for guessed letters:
guesses = []

# Game loop
play = True

while play:
    print(blank)
    print(f"*** LIVES LEFT: {lives} ***")
    guess = input("Guess a letter: ")

    if guess.lower() in fraze and guess.lower() not in guesses:
        guesses.append(guess.lower())
        for index, i in enumerate(fraze):
            if i.lower() == guess.lower():
                blank = blank[:index] + guess + blank[index + 1:]
                if "_" not in blank:
                    print("*** YOU WIN ***")
    elif guess.lower() in guesses:
        print(f"*** YOU ALREADY GUESSED LETTER: {guess}")
    else:
        guesses.append(guess.lower())
        lives -= 1
        if lives == 0:
            print("*** GAME OVER ***")
            print(f"*** THE FRAZE WAS: {fraze}")
            play = False

