import pandas as pd
import random


data = pd.read_csv('nato_phonetic_alphabet.csv')

print("\n*** WELCOME TO NATO ALPHABET HELPER ***")
print("-" * 40)

word = input('Enter a word: ').upper()

nato_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}

nato_word = [nato_alphabet[letter] for letter in word]

print('Word in nato phonetic alphabet:\n', nato_word)
print("-" * 40)