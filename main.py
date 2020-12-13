from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=800)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange']
start_y = 350

turtles = []
count = 0
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.turtlesize(2,2,1)
    turtle.color(color)
    turtle.penup()
    turtle.goto(-350,start_y)
    count += 1
    start_y -= 100
    turtles.append(turtle)

race_on = True
while race_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))

        if turtle.xcor() >= 370:
            turtle.goto(0, 0)
            race_on = False
    

screen.exitonclick()