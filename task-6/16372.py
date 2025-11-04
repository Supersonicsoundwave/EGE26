from turtle import *

tracer(False)
screensize(2000, 2000)
m = 10
dot(5, 'red')

lt(90)

for i in range(2):
    fd(23 * m)
    lt(90)
    bk(27 * m)
    lt(90)

up()
bk(5 * m)
rt(90)
fd(11 * m)
lt(90)
down()

dot(5, 'red')
for i in range(2):
    fd(26 * m)
    rt(90)
    fd(32 * m)
    rt(90)

up()
for x in range(0, 45):
    for y in range(-6, 25):
        goto(x * m, y * m)
        dot(3, 'blue')

update()
done()
