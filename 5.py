import turtle
import random


def tree(branchLen, t):
    if branchLen > 5:
        # 1. Толщина ветвей
        t.pensize(max(1, branchLen / 10))

        # 2. Цвет и листья
        if branchLen < 20:
            t.color("green")
        else:
            t.color("brown")

        t.forward(branchLen)

        # 3. Случайный угол
        angle = random.randint(15, 45)
        # 4. Случайное уменьшение длины
        delta = random.randint(10, 20)

        t.right(angle)
        tree(branchLen - delta, t)

        t.left(angle * 2)
        tree(branchLen - delta, t)

        t.right(angle)
        t.backward(branchLen)


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    myWin.bgcolor("white")
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(150)
    t.down()

    tree(90, t)

    myWin.exitonclick()


if __name__ == "__main__":
    main()