from turtle import *


tracer(False)
screensize(2000, 2000)
m = 10
lt(90)

dot(10, 'red')
for i in range(5):
    fd(37 * m)
    rt(90)
    fd(44 * m)
    rt(90)

up()
bk(18 * m)
rt(90)
fd(29 * m)
lt(90)
down()

dot(10, 'green')
for i in range(5):
    fd(31 * m)
    rt(90)
    fd(35 * m)
    rt(90)

up()
for x in range(0, 25):
    for y in range(0, 40):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
