from turtle import Turtle , Screen
import time

screen = Screen()
screen.setup(width = 600 ,height = 600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0) # 0 to switch off the screen tracing now you have to update the screen manually

segment_1 = Turtle("square")
segment_1.color("white")
segment_1.penup()

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.penup()
segment_2.goto(-20,0)


segment_3 = Turtle("square")
segment_3.color("white")
segment_3.penup()
segment_3.goto(-40,0)




segments = [segment_1, segment_2, segment_3]

game_is_on = True

while game_is_on:
    
        
    screen.update()
    time.sleep(1)


    for seg in range(len(segments)-1,0,-1): #(2,0,-1)
        new_x = segments[seg-1].xcor() #segment_2.xcor()
        new_y = segments[seg-1].ycor() #segment_2.ycor()
        segments[seg].goto(new_x,new_y) #segment_3.goto(segment_2.xcor(),segment_2.ycor())
    
    segments[0].forward(20)










screen.exitonclick()
