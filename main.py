#todo 1:Create snake body and screen setup
#todo 2:Move the snake
#todo 3:control the snake
#todo 4: Create food
#todo 5:create a scoreboard
#todo 6:detect collision with wall
#todo 7:detect collision with snakes body

import time
from turtle import Screen
from snake import Snake
from food import Food


screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
from scoreboard import ScoreBoard

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

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

    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        is_game_on= False
        scoreboard.game_over()

    for segment in snake.segments:

        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            is_game_on= False
            scoreboard.game_over()






screen.exitonclick()
