from turtle import Turtle, Screen
from random import randint

race_on = False
screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=400)
colors = ["red", "white", "orange", "cyan", "yellow"]
x_coordinate = -240
y_coordinate = -150
all_racer = []

for _ in range(5):
    y_coordinate += 50
    racer_ = Turtle(shape="turtle")
    racer_.speed("slow")
    all_racer.append(racer_)
    racer_.penup()
    racer_.color(colors[_])
    racer_.goto(x_coordinate, y_coordinate)
user_guess = screen.textinput(title="Make your guess", prompt="Which Turtle will win the race? Enter a color:")

if user_guess:
    race_on = True

while race_on:
    for racer in all_racer:
        if racer.xcor() > 230:
            race_on = False
            winning_colors = racer.pencolor()
            if winning_colors == user_guess:
                print(f"Congratulations you've won {winning_colors} turtle won the race")
            else:
                print(f"You've lost {winning_colors} turtle won the race")
        distance = randint(0, 5)
        racer.forward(distance)

screen.exitonclick()
