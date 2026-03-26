from functions import *


print("*** WELCOME TO HIGHER LOWER ***")
start = input("Are you ready to start? (y/n): ").lower()

play = start_game(start)
score = 0

while play:
    print("Playing...")


    print("*** WHICH BOOK HAS MORE WORDS? ***")
    book1 = choose_item()
    book2 = choose_item()
    print(f'A) "{book1['book_title']}" by {book1['author']} an author from {book1['country']}\n\n*** OR ***\n\nB) "{book2['book_title']}" by {book2['author']} an author from {book2['country']}\n')
    choice = input("--> ").lower()
    choice_approved = False
    while not choice_approved:
        if choice == 'a':
            choice_approved = True
        elif choice == 'b':
            choice_approved = True
        else:
            choice_approved = False
            print("Sorry, I didn't understand that. Please try again.")
            choice = input("--> ").lower()
    if choice == "a":
        choice = book1
    elif choice == "b":
        choice = book2
    higher_book = check_higher(book1, book2)
    if check_choice(higher_book, choice):
        score += 1
    else:
        play = False

