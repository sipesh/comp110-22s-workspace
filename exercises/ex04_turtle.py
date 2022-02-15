"""Drawing a house with three windows."""

__author__ = "730469262"

from turtle import Turtle, colormode, done, end_fill
from random import randint


def draw_a_triangle(a_triangle: Turtle, x: float, y: float, width: float) -> None:
    """Makes Roof of house."""
    triangle: Turtle = Turtle()
    triangle.penup()
    triangle.goto(x, y)
    triangle.pendown()
    i: int = 0
    triangle.fillcolor("blue")
    triangle.begin_fill()
    while(i < 3):
        triangle.forward(width)
        triangle.left(120)
        i = i + 1
    triangle.end_fill()


def draw_a_rectangle(a_rectangle: Turtle, x: float, y: float, width: float) -> None:
    """Draws the base of the house."""
    rectangle: Turtle = Turtle()
    rectangle.penup()
    rectangle.goto(x, y)
    rectangle.pendown()
    i: int = 0
    rectangle.fillcolor("maroon")
    rectangle.begin_fill()
    while(i < 4):
        rectangle.begin_fill()
        rectangle.forward(130)
        rectangle.left(90)
        i = i + 1
    rectangle.end_fill()


def draw_window(a_window: Turtle, x: float, y: float, width: float) -> None:
    """Draws windows."""
    t: Turtle = Turtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    i: int = 0
    t.fillcolor("gold")
    t.begin_fill()
    while(i < 4):
        t.forward(20)
        t.left(90)
        i = i + 1
    t.end_fill()


def tree_circle(treebase: Turtle, x: float, y: float, width: float) -> None:
    """Draws trees."""
    treebase.penup()
    treebase.goto(x, y)
    treebase.pendown()
    treebase.fillcolor("green")
    treebase.begin_fill()
    treebase.circle(40) 
    treebase.end_fill()


def treestump(tree_stump: Turtle, x: float, y: float, width: float) -> None:
    """Drawing a treestump for the tree."""
    stump: Turtle = Turtle()
    stump.penup()
    stump.goto(x, y)
    stump.pendown()
    stump.pencolor("pink")
    i: int = 0
    stump.fillcolor("brown")
    stump.begin_fill()
    while(i < 4):
        stump.forward(30)
        stump.left(90)
        i = i + 1
    stump.end_fill()


def draw_stars(x: float, y: float) -> None:
    """Draw stars."""
    stars: Turtle = Turtle()
    stars.penup()
    stars.goto(x, y)
    stars.pendown()
    turns = 5
    while turns > 0:
        stars.forward(25)
        stars.left(145)
        turns = turns - 1


rand_stars = 0
while rand_stars < 5:
    x = randint(-200, 200)
    y = randint(-200, 100)
    draw_stars(x, y)
    rand_stars = rand_stars + 1 


def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    draw_a_triangle(ertle, 120, 150, 200)
    draw_a_rectangle(ertle, 160, 20, -200)
    draw_window(ertle, 200, 220, 45)
    draw_window(ertle, 180, 80, -40)
    draw_window(ertle, 250, 80, -40)
    treestump(ertle, -11, 50, -40)
    tree_circle(ertle, 30, 80, -40)
    tree_circle(ertle, -10, 80, -40)
    tree_circle(ertle, 10, 120, -40)
    draw_stars(x, y)
    done()


main()
