from turtle import *


tracer(False)
screensize(3000, 3000)
lt(90)
m = 15

dot(5, 'red')
for i in range(2):
    fd(3 * m)
    rt(90)
    fd(20 * m)
    rt(90)

up()
bk(8 * m)
rt(90)
fd(9 * m)
lt(90)
down()

dot(5, 'green')
for i in range(2):
    fd(16 * m)
    rt(90)
    fd(8 * m)
    rt(90)

up()
for x in range(9, 18):
    for y in range(0, 4):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
