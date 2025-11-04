from turtle import *


tracer(False)
screensize(2000, 2000)
m = 5
lt(90)

dot(5, 'red')
for i in range(3):
    fd(27 * m)
    rt(90)
    fd(12 * m)
    rt(90)

up()
fd(4 * m)
rt(90)
fd(6 * m)
lt(90)
down()

dot(5, 'red')
for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)

up()
for x in range(0, 20):
    for y in range(0, 35):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
