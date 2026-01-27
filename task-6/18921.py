from turtle import *


tracer(False)
screensize(3000, 300)
lt(90)
m = 20

dot(5, 'red')
for i in range(13):
    fd(13 * m)
    rt(90)
    fd(5 * m)

up()
rt(90)
fd(7 * m)
lt(90)
fd(10 * m)
down()

dot(5, 'green')
for i in range(23):
    fd(8 * m)
    lt(90)
    fd(11 * m)
    lt(90)

up()
for x in range(30):
    for y in range(-5, 30):
        goto(x * m, y * m)
        dot(3, 'white')

update()
done()
