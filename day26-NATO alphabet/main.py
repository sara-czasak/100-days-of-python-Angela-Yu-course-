
import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
letters = data['letter'].to_list()
codes = data['code'].to_list()

# to_nato_alphabet = input('Enter word you: ')
