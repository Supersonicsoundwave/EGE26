from turtle import *


screensize(2000, 2000)
m = 30
lt(90)

dot(10, 'red')
rt(270)
for i in range(2):
    fd(8 * m)
    rt(120)

rt(120)

for i in range(2):
    rt(120)
    fd(3 * m)
    rt(240)

rt(240)

for i in range(2):
    fd(14 * m)
    rt(120)

update()
done()
