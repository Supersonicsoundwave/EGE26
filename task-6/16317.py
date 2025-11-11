from turtle import *


tracer(False)
screensize(2000, 2000)
m = 10
lt(90)

dot(5, 'red')
for i in range(2):
    fd(21 * m)
    rt(90)
    fd(27 * m)
    rt(90)

up()
fd(9 * m)
rt(90)
fd(10 * m)
lt(90)
down()

dot(5, 'green')
for i in range(2):
    fd(86 * m)
    rt(90)
    fd(47 * m)
    rt(90)

up()
for x in range(0, 40):
    for y in range(0, 40):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
