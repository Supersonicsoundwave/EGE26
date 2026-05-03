from turtle import *


tracer(False)
screensize(3000, 3000)
m = 15
lt(90)
rt(45)
dot(5, 'red')
for i in range(3):
    rt(45)
    fd(10 * m)
    rt(45)
dot(5, 'orange')
rt(315)
fd(10 * m)
rt(90)
dot(5, 'yellow')
fd(20 * m)
rt(90)
dot(5, 'green')
for i in range(2):
    fd(10 * m)
    rt(90)

up()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
