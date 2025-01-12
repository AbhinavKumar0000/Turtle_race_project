from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title= "Make your bet :", prompt= "Which tutle will win the race? Enter a color :")
all_kachua = []

color = ["green","blue","black","red","pink","yellow"]
y1 = -180
for i in color:
    kachua = Turtle(shape="turtle")
    kachua.penup()
    kachua.color(i)
    kachua.goto(x= -230,y= y1)
    y1+=66
    all_kachua.append(kachua)
if user_bet:
    is_race_on = True
while is_race_on:
    for i in all_kachua:
        if i.xcor() > 230:
            won = i.color()
            is_race_on = False

        rand_distance = random.randint(0,10)
        i.forward(rand_distance)
if won[1] == user_bet.lower():
    print(f"{won[1]} won\nYou have won the bet!")
else:
    print(f"{won[1]} won\nYou have lost the bet")

screen.exitonclick()