from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=800)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']
start_ys = [-150, -100, -50, 0, 50, 100, 150]

turtles = []
count = 0
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(-350,start_ys[count])
    count += 1
    turtles.append(turtle)

race_on = True
while race_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 380:
            print(f"{turtle.color} won")
            race_on = False

screen.exitonclick()