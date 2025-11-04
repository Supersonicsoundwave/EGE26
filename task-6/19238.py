from turtle import *


tracer(False)
screensize(2000, 2000)
m = 15
lt(90)

dot(5, 'red')
for i in range(8):
    fd(16 * m)
    rt(90)
    fd(22 * m)
    rt(90)

up()
fd(5 * m)
rt(90)
fd(5 * m)
lt(90)
down()

dot(5, 'red')
for i in range(8):
    fd(52 * m)
    rt(90)
    fd(77 * m)
    rt(90)

pu()
for x in range(-1, 25):
    for y in range(-1, 25):
        goto(x * m, y * m)
        dot(10, 'white')

update()
done()



