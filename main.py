from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(width=500, height=450)

colors = ["blue", "red", "magenta", "orange", "black", "green", "cyan", "violet"]
positions = [100, 70, 40, 10, -20, -50, -80, -110]

user = screen.textinput(title="Make your bet", prompt=f"Which turtle do you think will win the race? Enter a color from {colors}: ")

if user:
    user = user.strip().lower()
    if user not in colors:
        print("Invalid color entered!")
    else:
        race = True

t_list = []

for i in range(8):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=-230, y=positions[i])
    t_list.append(t)

finish_line = Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(230, 125)
finish_line.right(90)
finish_line.pendown()
finish_line.pensize(4)
for _ in range(12):
    finish_line.forward(10)
    finish_line.penup()
    finish_line.forward(10)
    finish_line.pendown()


if race:
    while race:
        for turtle in t_list:
            if turtle.xcor() > 230:
                race = False
                winning_color = turtle.pencolor()
                if winning_color == user:
                    print(f"🎉 Congrats! Your turtle '{winning_color}' won the race!")
                else:
                    print(f"😢 Sorry, your turtle lost. The winner was '{winning_color}'.")
                break  # Stop checking once a winner is found
            rand_dist = random.randint(0, 10)
            turtle.forward(rand_dist)

screen.exitonclick()


