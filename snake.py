from turtle import Turtle

MOVE_DISTANCE = 20

up = 90
down = 270
left = 180
right = 0
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.square_list = []
        self.create_snake()
        self.head = self.square_list[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):

        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.square_list.append(square)

    def extend(self):
        self.add_segment(self.square_list[-1].position())

    def move(self):
        for squ in range(len(self.square_list) - 1, 0, -1):
            new_x = self.square_list[squ - 1].xcor()
            new_y = self.square_list[squ - 1].ycor()
            self.square_list[squ].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)