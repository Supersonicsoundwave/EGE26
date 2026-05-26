from turtle import *


tracer(False)
screensize(3000, 3000)
m = 15
lt(90)

dot(5, 'red')
for i in range(3):
    fd(5 * m)
    lt(270)
    bk(8 * m)
    lt(270)
up()
fd(2 * m)
rt(90)
bk(3 * m)
lt(90)
down()
dot(5, 'orange')
for i in range(3):
    fd(4 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
fd(4 * m)
rt(180)
bk(2 * m)
down()
dot(5, 'green')
for i in range(2):
    fd(5 * m)
    rt(90)
    fd(7 * m)
    rt(90)

up()
for x in range(-20, 10):
    for y in range(-10, 10):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
