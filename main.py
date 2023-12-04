import turtle
from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet",prompt="Which turtle are you betting on ?" )
colours = ["red","green","grey","purple","yellow"]

is_race_on = False

y_pos = [100, 60, 20, -20, -60]
all_turtles = []
for turtle_index in range(0,5):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y_pos[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You have won the race . The {winning_colour} turtle is the winner !")
            else :
                print(f"You ve lost ! the {winning_colour} turtle is the winner !")



        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


my_screen.exitonclick()