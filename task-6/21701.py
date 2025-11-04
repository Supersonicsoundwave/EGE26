from turtle import *


tracer(False)
screensize(2000, 2000)
m = 10
lt(90)

dot(5, 'red')
for i in range(2):
    fd(28 * m)
    rt(90)
    fd(18 * m)
    rt(90)

up()
fd(14 * m)
rt(90)
fd(10 * m)
lt(90)
down()

dot(5, 'red')
for i in range(2):
    fd(30 * m)
    rt(90)
    fd(7 * m)
    rt(90)

pu()
for x in range(0, 20):
    for y in range(0, 50):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
