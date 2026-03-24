from brain import *


print("*** WELCOME TO YOU SILENT AUCTION ***")

bidders = {}
bidding = True

while bidding:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidders[name] = bid
    next_bid = input("Is anyone else bidding? (Y/N) ").lower()
    if next_bid == "y":
        print("\n" * 20)
    else:
        print("\n" * 20)
        bidding = False

bidder = choose_winner(bidders)

print(f"The winner is {bidder.title()} with a bid of ${bidders[bidder]}.")
