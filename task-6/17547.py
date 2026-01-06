from turtle import *


screensize(5000, 5000)
speed(4)
m = 10

for i in range(3):
    fd(7 * m)
    rt(90)
    fd(12 * m)
    rt(90)

pu()
fd(4 * m)
rt(90)
fd(6 * m)
lt(90)
pd()

for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)

pu()
for x in range(-10, 10):
    for y in range(-10, 10):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()
