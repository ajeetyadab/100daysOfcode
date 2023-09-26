from turtle import Turtle , Screen
from snake import Snake
import time



screen = Screen()
screen.setup(width = 600 ,height = 600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0) # 0 to switch off the screen tracing now you have to update the screen manually


game_is_on = True
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
    

while game_is_on:
    screen.update()
    time.sleep(.3)
    snake.move()
    
    
    




   










screen.exitonclick()
