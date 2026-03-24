from turtle import *


tracer(False)
screensize(3000, 3000)
lt(90)
m = 15

dot(5, 'red')
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(20 * m)
    rt(90)

up()
bk(4 * m)
rt(90)
fd(7 * m)
lt(90)
down()

dot(5, 'green')
for i in range(4):
    fd(8 * m)
    lt(90)
    fd(12 * m)
    lt(90)

up()
fd(10 * m)
down()

dot(5, 'pink')
for i in range(4):
    fd(12 * m)
    rt(90)

up()
for x in range(7, 20):
    for y in range(6, 11):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
