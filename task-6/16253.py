from turtle import *


tracer(False)
screensize(10000, 10000)
m = 10
lt(90)

dot(5, 'red')
rt(45)
for i in range(10):
    rt(45)
    fd(203 * m)
    rt(45)

up()
bk(40 * m)
rt(45)
down()
dot(5, 'red')
for i in range(5):
    fd(20 * m)
    lt(90)

up()
for x in range(200, 240):
    for y in range(-200, -170):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
