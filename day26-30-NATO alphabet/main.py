import pandas as pd


data = pd.read_csv('nato_phonetic_alphabet.csv')

print("\n*** WELCOME TO NATO ALPHABET HELPER ***")
print("-" * 40)

nato_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

finished = False
while not finished:
    done = False
    while not done:
        word = input('Enter a word: ').upper()
        try:
            nato_word = [nato_alphabet[letter] for letter in word]
            print('Word in nato phonetic alphabet:\n', nato_word)
            print("-" * 40)
            done = True
        except KeyError:
            print("Please enter a valid word containing only letters.")
    again = input("\nDo you need another word translated to the NATO alphabet?").lower()
    if again == 'no':
        finished = True

print("-" * 40)
print('*** SEE YOU NEXT TIME ***')
print("-" * 40)