#todo 1:Create snake body and screen setup
#todo 2:Move the snake
#todo 3:control the snake
#todo 4: Create food
#todo 5:create a scoreboard
#todo 6:detect collision with wall
#todo 7:detect collision with snakes body

import time
from turtle import Turtle,Screen
from snake import Snake

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake=Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on= True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()
