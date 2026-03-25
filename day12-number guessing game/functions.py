

def set_difficulty(choice):
    if choice == 1:
        lives = 10
    else:
        lives = 5
    return lives

def check_guess(guess, number, lives):
    if guess == number:
        print(f"Congrats, you won!\n* The number was {number}.\n* You still have {lives} lives left!.")
        return lives
    elif guess > number:
        print("Too high!")
        lives -= 1
        return lives
    elif guess < number:
        print("Too low!")
        lives -= 1
        return lives

