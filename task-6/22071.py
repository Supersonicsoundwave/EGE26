from turtle import *


tracer(False)
screensize(3000, 3000)
m = 15
lt(90)

dot(6, 'red')
fd(30 * m)
lt(60)
fd(24 * m)
rt(240)

fd(54 * m)
lt(120)
fd(24 * m)
lt(60)

up()
fd(30 * m)
rt(90)
fd(20 * m)
lt(90)
down()

dot(6, 'green')
for i in range(17):
    fd(6 * m)
    lt(90)
    fd(80 * m)
    lt(90)

up()
for x in range(-40, 30):
    for y in range(-10, 100):
        goto(x * m, y * m)
        dot(4, 'white')
update()
done()
