from turtle import *


tracer(False)
m = 10
screensize(2000, 2000)
lt(90)

dot(5, 'red')
for i in range(6):
    fd(33 * m)
    rt(90)
    fd(20 * m)
    rt(90)

up()
fd(3 * m)
rt(90)
fd(9 * m)
lt(90)
down()

dot(5, 'green')
for i in range(6):
    fd(24 * m)
    rt(90)
    fd(25 * m)
    rt(90)

up()
for x in range(9, 21):
    for y in range(3, 28):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()

