import random

# Building deck of cards
deck = [i for i in range(1, 12)]
deck = deck * 4


print("*** WELCOME TO BLACKJACK ***")
breaking_line =  "-"*30
print(breaking_line)


def choose_starting_cards(deck):
    dealer_hand = random.choices(deck, k=2)
    player_hand = random.choices(deck, k=2)
    return dealer_hand, player_hand


done = False
while not done:
    dealer_hand, player_hand = choose_starting_cards(deck)
    print(breaking_line)
    print(f"Dealer's first card: {dealer_hand[0]}")
    print(f"Your cards: {player_hand} (total: {sum(player_hand)})")
    if sum(player_hand) == 21 and sum(dealer_hand) == 21:
        print(f"Dealer's cards: {dealer_hand} (total: {sum(dealer_hand)})")
        print(f"Your cards: {player_hand} (total: {sum(player_hand)})")
        print("*** BLACKJACK TIE ***")
        done = True
    elif sum(player_hand) == 21:
        print(f"Dealer's cards: {dealer_hand} (total: {sum(dealer_hand)})")
        print(f"Your cards: {player_hand} (total: {sum(player_hand)})")
        print("*** BLACKJACK ***")
        print("*** YOU WIN ***")
        done = True
    choice = input("Would you like to get another card? (y/n) ").lower()
    print(breaking_line)
    if choice == "y":
        player_hand.append(random.choice(deck))
        print(f"Dealer's first card: {dealer_hand[0]}")
        print(f"Your cards: {player_hand} (total: {sum(player_hand)})")
        if sum(player_hand) > 21:
            print("*** BUST! ***")
            print(f"Dealer's cards: {dealer_hand} (total: {sum(dealer_hand)})")
            print(f"Your cards: {player_hand} (total: {sum(player_hand)})")
            done = True
    else:
        done = True
        print(f"Dealer's cards: {dealer_hand} (total: {sum(dealer_hand)})")
        print(f"Your cards: {player_hand} (total: {sum(player_hand)})")
        while sum(dealer_hand) < 17:
            dealer_hand.append(random.choice(deck))
            print(f"Dealer's cards: {dealer_hand} (total: {sum(dealer_hand)})")
            print(f"Your cards: {player_hand} (total: {sum(player_hand)})")
        if sum(dealer_hand) > 21:
            print("*** DEALER BUST! ***")
            print("*** YOU WIN ***")
        elif sum(dealer_hand) > sum(player_hand):
            print("*** YOU LOSE! ***")
        elif sum(dealer_hand) < sum(player_hand):
            print("*** YOU WIN! ***")
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again == "y":
            done = False
        else:
            print("*** THANKS FOR PLAYING ***")





