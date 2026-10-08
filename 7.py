import turtle
import random


def mountain(t, x1, y1, x2, y2, displacement, depth):
    if depth == 0:
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)
        return

    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2

    my += random.uniform(-displacement, displacement)

    mountain(t, x1, y1, mx, my, displacement / 2, depth - 1)
    mountain(t, mx, my, x2, y2, displacement / 2, depth - 1)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    win.bgcolor("lightblue")
    t.speed(0)
    t.pensize(2)
    t.color("black")

    x1, y1 = -300, -100
    x2, y2 = 300, -100

    mountain(t, x1, y1, x2, y2, displacement=180, depth=7)

    win.exitonclick()


if __name__ == "__main__":
    main()