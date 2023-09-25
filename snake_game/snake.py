STARTING_POSITION = [(0,0),(-20,0),(-40,0)] # constants veriables are written in caps
from turtle import Turtle

class Snake :
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments)-1,0,-1): #(2,0,-1)
            new_x = self.segments[seg-1].xcor() #segment_2.xcor()
            new_y = self.segments[seg-1].ycor() #segment_2.ycor()
            self.segments[seg].goto(new_x,new_y) #segment_3.goto(segment_2.xcor(),segment_2.ycor())
        
        self.segments[0].forward(20)





