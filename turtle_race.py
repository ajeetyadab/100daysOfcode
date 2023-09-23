from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width= 500, height= 400)

user_bet = screen.textinput(title="enter your bet" , prompt="which turtle will win the race")

turtle1 = Turtle("turtle")
turtle1.color("red")


turtle2 = Turtle("turtle")
turtle2.color("blue")

turtle3 = Turtle("turtle")
turtle3.color("yellow")

turtle4 = Turtle("turtle")
turtle4.color("green")

turtle5 = Turtle("turtle")
turtle5.color("black")

positions_y = [-50, -20 , 10 , 40 , 70]
positions_x = -240

turtle =[turtle1,turtle2,turtle3,turtle4,turtle5]
movement = [20,10,40,0,10,20,10,20]


for i in range(0,len(positions_y)):
    turtle[i].penup()
    turtle[i].setpos(positions_x,positions_y[i])

condition = True

while condition:
    for turtles in turtle:
        turtles.forward(random.choice(movement))
        winning_pos = turtles.position()
        if winning_pos[0] >= 250:
            print(f" turtles : {turtle.index(turtles)+1} won")
            condition = False
    

    
    


















screen.exitonclick()
 