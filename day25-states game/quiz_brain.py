import pandas as pd


data = pd.read_csv('50_states.csv')

data_dict = data.to_dict()
all_states = list(data_dict['state'].values())
all_x = list(data_dict['x'].values())
all_y = list(data_dict['y'].values())

def check_if_state(answer):
    if answer.capitalize() in all_states:
        index = all_states.index(answer.capitalize())
        return all_x[index], all_y[index]
    return False