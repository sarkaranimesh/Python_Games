from snake import Snake
from turtle import  Screen
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width = 600, height =600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
game_is_on = True


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on ==True:
    screen.update()
    time.sleep(0.1)

    snake.move()
#todo: collison with food
    if snake.head.distance(food) < 15:
        print("no nom nom")
        food.refresh()
        snake.extend()
        score.calculate_score()
# detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False
    # detect collision with tail
    for segment in snake.segments[1:len(snake.segments)-1]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score.game_over()




        # game_is_on= False












screen.exitonclick()