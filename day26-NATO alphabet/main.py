import pandas
import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')
data = data.to_dict()

to_nato_alphabet = input('Enter word you: ')
