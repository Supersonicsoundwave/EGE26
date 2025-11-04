from turtle import *

tracer(False)
screensize(2000, 2000)
m = 15
lt(90)

for i in range(2):
    fd(5 * m)
    lt(90)
    bk(13 * m)
    lt(90)

pu()
bk(10 * m)
rt(90)
fd(9 * m)
lt(90)
pd()

for i in range(2):
    fd(11 * m)
    rt(90)
    fd(7 * m)
    rt(90)

pu()
for x in range(-3, 20):
    for y in range(-15, 7):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
