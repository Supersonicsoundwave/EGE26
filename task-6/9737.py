from turtle import *


screensize(2000, 2000)
tracer(False)
m = 25
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(18 * m)
    rt(90)

pu()
fd(5 * m)
rt(90)
fd(7 * m)
lt(90)
pd()

for i in range(2):
    fd(10 * m)
    rt(90)
    fd(7 * m)
    rt(90)

pu()
for x in range(-5, 25):
    for y in range(-25, 5):
        goto(x * m, y * m)
        dot(3, 'red')


update()
done()




