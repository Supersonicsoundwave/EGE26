from turtle import *


tracer(False)
screensize(2000, 2000)
m = 40
lt(90)

rt(90)
for i in range(7):
    rt(45)
    fd(11 * m)
    rt(45)

up()
for x in range(-10, 10):
    for y in range(-20, 3):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
