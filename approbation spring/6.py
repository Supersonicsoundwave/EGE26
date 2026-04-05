from turtle import *


tracer(False)
screensize(3000, 3000)
m = 15

# точки плюс 1 !!!!!!!!!!!!
dot(5, 'red')
for i in range(4):
    fd(10 * m)
    rt(270)

up()
fd(3 * m)
rt(270)
fd(5 * m)
rt(90)
down()

dot(5, 'green')
for i in range(2):
    fd(10 * m)
    rt(270)
    fd(12 * m)
    rt(270)

up()
for x in range(3, 11):
    for y in range(5, 11):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
