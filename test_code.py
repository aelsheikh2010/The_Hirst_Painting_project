import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)

screen = Screen()
tim = Turtle()

#draw a dashed line
# for _ in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#draw a list of shapes
# colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
#
#
# def draw_shapes(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         tim.color(random.choice(colors))
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape in range(3, 11):
#     draw_shapes(shape)


def random_color():
    """return a tuple of red green blue"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tup = (r, g, b)
    return color_tup


# directions = [0, 90, 180, 270]
# tim.pensize(8)
# tim.speed("fastest")
# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

tim.pensize(1)
tim.speed("fastest")


def draw_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(80)
        tim.setheading(tim.heading() + size_of_gap)


draw_circle(3)






screen = Screen()
screen.exitonclick()