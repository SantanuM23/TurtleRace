from turtle import Turtle, Screen
import random

colors = ["violet", "blue", "lightblue", "green", "yellow", "orange", "red"]

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
y_pos = -110
all_turtles = []

for turtle_index in range(len(colors)):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-220, y=y_pos)
    y_pos += 40
    all_turtles.append(tim)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! {winner} Turtle Finished First!!")
            else:
                print(f"You've Lost! {winner} Turtle Finished First!!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()