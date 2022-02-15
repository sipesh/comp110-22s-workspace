from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.penup()
leo.goto(45, 60)
leo.pendown()







leo.begin_fill()
i: int = 0
while (i < 3):
    leo.pencolor("pink")
    leo.fillcolor(32, 67, 93)
    leo.color("green", "yellow")

    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
