# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# print(colors)
# new_colors = []
import turtle
#import turtle

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors.append((r, g, b))
# print(new_colors)
# for color in range(len(colors)):
#     new_color = colors[color]
#     rgb = new_color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     new_colors.append((r, g, b))
# print(new_colors)


#color_list = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134), (115, 31, 46), (97, 150, 100), (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165), (25, 91, 65), (172, 205, 180)]

from turtle import Turtle, Screen
import random
color_list = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134), (115, 31, 46), (97, 150, 100), (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165), (25, 91, 65), (172, 205, 180)]
turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed('fastest')
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.left(90)
        tim.forward(50)
        tim.left(90)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()

