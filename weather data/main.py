# import csv
#
# with open(file='weather_data.csv') as file:
#     # data = file.readlines()
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         temp.append(int(row[1]))
#     print(temp)

import pandas

data = pandas.read_csv('weather_data.csv')
print(data['temp'].max)
