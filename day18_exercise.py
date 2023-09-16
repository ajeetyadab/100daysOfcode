# ex : 1drawing the circle

from turtle import Turtle, Screen
import random 

timmy_the_turtle = Turtle()
screen = Screen()

# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# ex:2 drawing dashed line


# color = ["red","blue","pink","yellow"]
# for i in range(20):
    
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.pendown()


#ex :3 drawing a triangle , square, pentagon , hexagon , heptagon , nonagon and decagon 



# screen.colormode(1)
# i = 3

# while True:
#     n = random.choice(range(255))
#     tup = (n,n,n)
#     angle = 360/i
#     for _ in range(i):
#         timmy_the_turtle.pencolor(tup)
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#     i = i +1
#     if i >10:
#         break


# ex 4 : drawing a random walk 
color = ["DeepSkyBlue","Cyan","DeepPink","Lavender","LavenderBlush","MediumSpringGreen","LightSlateGray"]


# timmy_the_turtle.width(10)
# timmy_the_turtle.speed("fastest")
# while True:
    
#     choice_color = random.choice(color)
#     timmy_the_turtle.pencolor(choice_color)
#     direction = random.choice([0,90,-90])
#     timmy_the_turtle.right(direction)
#     timmy_the_turtle.forward(15)


#ex:5 making spirograph 
tilt = 5
timmy_the_turtle.speed("fastest")
for i in range (72):
    timmy_the_turtle.pencolor(random.choice(color))
   
    timmy_the_turtle.circle(100)
    timmy_the_turtle.right(tilt)
    tilt =+ 5


screen.exitonclick()