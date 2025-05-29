# import colorgram
"""Extraction of the color from the color gram module"""
# rgb_colors = []
# colors = colorgram.extract('image.jpg',15)

# # print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

import turtle as t
import random
turtle = t.Turtle()
screen = t.Screen()

t.colormode(255)
color_list = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169)]
# print(turtle.heading())

turtle.hideturtle()
turtle.setheading(225)
turtle.penup()
turtle.forward(300)
turtle.setheading(0)
num_of_dots = 100


for dot_count in range(1, num_of_dots+1): 
    colour = random.choice(color_list)
    turtle.penup()
    turtle.dot(20, colour)
    turtle.forward(50)

    if dot_count % 10 == 0:    
        turtle.speed(0)     
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)




# for _ in range(10):
#     for i in range(10): 
#         colour = random.choice(color_list)
#         turtle.penup()
#         turtle.dot(20, colour)
#         turtle.forward(50)

#     # if     
#     turtle.speed(0)     
#     turtle.setheading(90)
#     turtle.forward(50)
#     turtle.setheading(180)
#     turtle.forward(500)
#     turtle.setheading(0)


screen.exitonclick()