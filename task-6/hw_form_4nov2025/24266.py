from turtle import *


tracer(False)
screensize(2000, 2000)


def f(x):
    m = 10
    lt(90)

    dot(10, 'red')
    for i in range(4):
        fd(x * m)
        rt(90)
        fd(48 * m)
        rt(90)

    up()
    fd(27 * m)
    rt(90)
    fd(24 * m)
    lt(90)
    down()

    dot(10, 'green')
    for i in range(4):
        fd(29 * m)
        rt(90)
        bk(18 * m)
        rt(90)

    up()
    for x in range(0, 30):
        for y in range(0, 40):
            goto(x * m, y * m)
            dot(8, 'white')

    update()
    done()


f(30)
