import random

print("*** LETS PLAY ROCK PAPER SCISSORS ***")

play = True

while play:
    user_choice = input("Up for a game of rock paper scissors?\n- Y\n- N\n").lower()
    if user_choice == "y":
        comp_choice = random.choice(["rock", "paper", "scissors"])
        user_choice = input("What do you choose?\n- rock\n- paper\n- scissors\n").lower()
        print(f"Computer choice: {comp_choice}")
        print(f"User choice: {user_choice}")
        if user_choice == comp_choice:
            print("*** IT'S A TIE ***")
        elif user_choice == "rock" and comp_choice == "scissors" or user_choice == "paper" and comp_choice == "rock" or user_choice == "scissors" and comp_choice == "paper":
            print("*** YOU WIN ***")
        else:
            print("*** YOU LOSE ***")
    elif user_choice == "n":
        print("Thanks for playing!")
        play = False
    else:
        print("Sorry, didn't catch that..")

print("*** SEE YOU NEXT TIME! ***")