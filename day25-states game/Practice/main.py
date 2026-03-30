import pandas as pd


data = pd.read_csv('weather_data.csv')

# print(data['temp'])
# print(list(data['temp']))

# data_dict = data.to_dict()
# # print(data_dict)
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# total = sum(temp_list)
# avg = total/len(temp_list)
# print(avg)

# print(data['temp'].min())

# print(data.condition)

# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# # print((monday.temp * 1.8) + 32)
#
# monday_temp = monday.temp[0]
# print(monday_temp)
# monday_temp_f = monday_temp * 1.8 + 32
# print(monday_temp_f)
#
# data_dict = {
#     'name': ['Sara', 'Oscar', 'Paula'],
#     'age': [31, 28, 67]
# }
#
# df = pd.DataFrame(data_dict)
# print(df)
#
# df.to_csv('new_data.csv')