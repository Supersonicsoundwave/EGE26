from turtle import *


screensize(2000, 2000)
tracer(False)
m = 20

for i in range(9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)

pu()
fd(1 * m)
rt(90)
fd(5 * m)
lt(90)
pd()

for i in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)

pu()
for x in range(0, 30):
    for y in range(-10, 2):
        goto(x * m, y * m)
        dot(3, 'purple')

update()
done()
