import colorgram
from turtle import Turtle , Screen 
import turtle
import random
colors = colorgram.extract("./Desktop/100daysofCode/hirst_painting.jpg", 30)


li = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tupe = (r,g,b)
    li.append(tupe)

print(li)

timmy = Turtle()
screen = Screen()
screen.colormode(255)

timmy.penup()
timmy.setposition(-330,-270)
timmy.pendown()

position = timmy.position()

position_y = -270

timmy.speed("fastest")
while True :
    for i in range(23):
        timmy.color(random.choice(li))
        timmy.dot(30)
        timmy.penup()
        timmy.forward(50)
        
    position_y = position_y + 50
    timmy.penup()
    timmy.setposition(-330, position_y)
    timmy.pendown()   
    




        


screen.exitonclick()