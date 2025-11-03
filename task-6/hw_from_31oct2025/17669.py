from turtle import *


screensize(3000, 3000)
tracer(False)
m = 20

for i in range(4):
    fd(19 * m)
    rt(90)
    fd(30 * m)
    rt(90)

pu()
fd(2 * m)
rt(90)
fd(8 * m)
lt(90)
pd()

for i in range(4):
    fd(93 * m)
    rt(90)
    fd(97 * m)
    rt(90)

pu()
for x in range(0, 30):
    for y in range(-30, 2):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()
