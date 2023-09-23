from turtle import Turtle , Screen

# tim = Turtle()
# screen =Screen()

# def move_forward():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key = "space" , fun = move_forward)

# screen.exitonclick()

#-----------------------------------------------------
#sketch sketch program
from turtle import Turtle , Screen
import turtle
tim = Turtle()

screen = Screen()
def move_forward():
    tim.forward(10)

def move_backward():
    tim.forward(-10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.setposition(0,0)
    tim.setheading(0)
    tim.pendown()


screen.listen()

screen.onkey(key = "w",fun=move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a" , fun = turn_right)
screen.onkey(key = "d" , fun = turn_left)
screen.onkey(key = "c" , fun = clear)







screen.exitonclick()
