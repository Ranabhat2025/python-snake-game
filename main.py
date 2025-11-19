from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.title("Mana's snake game")
screen.setup(width=600, height=600)
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    score.write_score()
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 55:
        food.refresh()
        snake.increase_snake()
        score.score_board()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    #detect collision with tail
    for seg in snake.segments[1:]:
    #     if seg == snake.head:
    #         pass

        if snake.head.distance(seg) < 10:
                score.reset()
                snake.reset()




screen.exitonclick()


