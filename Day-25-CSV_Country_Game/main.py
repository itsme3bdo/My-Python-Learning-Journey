# # import csv
# #
# # with open("weather_data.csv","r") as file:
# #     data = csv.reader(file)
# #     temp = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temp.append(int(row[1]))
# # print(temp)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
#
#
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# print( (int(monday_temp)* 9/5) + 32,"F")

import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame

gray=0
cinnamon = 0
black=0
Color={}

# Primary Fur Color
data = pandas.read_csv("Squirrel_Data.csv")
sq_color = data["Primary Fur Color"]

for x in sq_color:
    if x == "Gray":
        gray+=1
    elif x == "Cinnamon":
        cinnamon+=1
    elif x == "Black":
        black+=1

damn = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[gray,cinnamon,black]
}
final = pandas.DataFrame.from_dict(damn)
final.to_csv("squirrel_count.csv")

# print(damn)
