from turtle import *


tracer(False)
screensize(2000, 2000)
m = 30
lt(90)

dot(5, 'red')
rt(30)
for i in range(3):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)

up()
for x in range(-20, 1):
    for y in range(-20, 1):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
