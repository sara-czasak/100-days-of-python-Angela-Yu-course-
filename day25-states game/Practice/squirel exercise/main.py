# create csv that contains color count (gray, cinamon, white)
import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

all_colors = data['Primary Fur Color']

gray = data[data['Primary Fur Color'] == 'Gray']
red = data[data['Primary Fur Color'] == 'Cinnamon']
black = data[data['Primary Fur Color'] == 'Black']
print(len(gray), len(red), len(black))

data_dict = {
    "Fur Color": ['Gray', 'Red', 'Black'],
    "Count": [len(gray), len(red), len(black)]
}

data_dict = pd.DataFrame(data_dict)
data_dict.to_csv('data_dict.csv', index=False)