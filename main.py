import turtle as turd
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from settings import GameSettings

game_settings = GameSettings()
game_settings.get_game_mode()

print("Game is ON")


screen = turd.Screen()
screen.setup(width= 600,height= 600)
screen.bgcolor("black")
screen.title("My Snake Game.")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard(game_settings.has_walls)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_settings.game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect food
    if snake.head.distance(food)<15:
        score.add()
        score.high_score_reset()
        food.refresh()
        snake.grow()
    #Detect wall collision
    if game_settings.has_walls:
        if (
                snake.head.xcor()>=290 or snake.head.xcor()<=-290 or
                snake.head.ycor()>=280 or snake.head.ycor()<=-290
        ):
            score.reset()
            snake.game_over()
    else:
        # Wrap-around (no walls mode)
        if snake.head.xcor() >= 310:
            snake.head.setx(-290)
        elif snake.head.xcor() <= -310:
            snake.head.setx(290)
        elif snake.head.ycor() >= 265:
            snake.head.sety(-290)
        elif snake.head.ycor() <= -310:
            snake.head.sety(265)

    #Detect collision with tail
    for seg in snake.snake_body:
        if snake.head == seg:
            pass
        elif snake.head.distance(seg) < 10:
            score.reset()
            snake.game_over()




screen.exitonclick()