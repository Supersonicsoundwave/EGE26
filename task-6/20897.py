from turtle import *


tracer(False)
screensize(3000, 3000)
m = 10
lt(90)

dot(5, 'red')
for i in range(9):
    fd(27 * m)
    rt(90)
    fd(30 * m)
    rt(90)
up()
fd(3 * m)
rt(90)
fd(6 * m)
lt(90)
down()
dot(5, 'green')
for i in range(9):
    fd(77 * m)
    rt(90)
    fd(66 * m)
    rt(90)

up()
for x in range(0, 50):
    for y in range(0, 50):
        goto(x * m, y * m)
        dot(3, 'white')

update()
done()