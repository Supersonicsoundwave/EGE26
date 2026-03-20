from turtle import *


tracer(False)
screensize(3000, 3000)
m = 15
lt(90)

dot(5, 'red')
for i in range(4):
    fd(36 * m)
    rt(90)
    fd(41 * m)
    rt(90)

up()
rt(90)
fd(20 * m)
lt(90)
fd(20 * m)
down()

dot(5, 'green')
for i in range(4):
    fd(25 * m)
    rt(90)

up()
fd(7 * m)
lt(90)
fd(7 * m)
rt(90)
down()

dot(5, 'orange')
for i in range(7):
    fd(16 * m)
    rt(90)

up()
for x in range(20, 30):
    for y in range(27, 37):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
