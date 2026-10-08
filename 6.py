import turtle

def koch(t, length, order):
    if order == 0:
        t.forward(length)
    else:
        length /= 3
        koch(t, length, order - 1)
        t.left(60)
        koch(t, length, order - 1)
        t.right(120)
        koch(t, length, order - 1)
        t.left(60)
        koch(t, length, order - 1)


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    win.bgcolor("white")
    t.speed(0)
    t.pensize(2)
    t.color("blue")

    t.up()
    t.goto(-200, 0)
    t.down()

    koch(t, 400, 4)

    win.exitonclick()


if __name__ == "__main__":
    main()