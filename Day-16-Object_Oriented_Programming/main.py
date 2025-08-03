# from turtle import Turtle,Screen
# moody = Turtle()
# print(moody)
# moody.shape("turtle")
# moody.color("chartreuse4")
# moody.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikacu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align="l"



print(table)

