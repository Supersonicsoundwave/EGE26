from turtle import *


KL = [[], []]
for i in open('27_A.txt').readlines()[1:]:
    x, y = [float(e) for e in i.replace(',', '.').split()]
    if y > 15:
        KL[0] += [(x, y)]
    else:
        KL[1] += [(x, y)]

# tracer(False)
# up()
# col = ['green', 'red']
# for i in range(2):
#     for x, y in KL[i]:
#         goto(x * 10, y * 10)
#         dot(3, col[i])
# done()

def dist(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5


def smDist(x1, y1, kl):
    sm = 0
    for x2, y2 in kl:
        sm += dist(x1, y1, x2, y2)
    return sm


def center(kl):
    x, y = 0, 0
    mn = 10**10
    for x1, y1 in kl:
        smd = smDist(x1, y1, kl)
        if smd < mn:
            x, y = x1, y1
    return x, y


x1, y1 = center(KL[0])
x2, y2 = center(KL[1])
print((x1 + x2) * 10000, (y1 + y2) * 10000)
