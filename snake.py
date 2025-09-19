from turtle import Turtle



class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]

    def create_snake(self):
        for i in range(3):
            seg = Turtle("square")
            seg.up()
            seg.color("white")
            seg.goto(-i * 20, 0)
            self.snake_body.append(seg)

    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            x = self.snake_body[seg - 1].xcor()
            y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def grow(self):
        snake = Turtle("square")
        snake.goto(self.tail.pos())
        snake.color("white")
        snake.penup()
        snake.speed("fastest")
        self.snake_body.append(snake)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def game_over(self):
        g_o = Turtle()
        g_o.penup()
        g_o.goto(0,0)
        g_o.write("GAME OVER.", align="center", font=("Courier", 24, "normal"))