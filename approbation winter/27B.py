from turtle import *


KL = [[], [], [], []]
for i in open('27_B.txt').readlines()[1:]:
    x, y = [float(e) for e in i.replace(',', '.').split()]
    if 0 < x < 10:
        KL[0] += [(x, y)]
    elif 10 < x < 19:
        KL[1] += [(x, y)]
    elif 19 < x < 27:
        KL[2] += [(x, y)]
    else:
        KL[3] += [(x, y)]

# tracer(False)
# screensize(3000, 3000)
# up()
# col = ['green', 'red', 'blue', 'black']
# for i in range(4):
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


centers = [center(KL[0]), center(KL[1]), center(KL[2])]
mn = 10000000000000
mx = 0
for x1, y1 in centers:
    for x2, y2 in centers:
        if (x1, y1) != (x2, y2):
            mn = min(mn, dist(x1, y1, x2, y2))
            mx = max(mx, dist(x1, y1, x2, y2))
print(mn * 10000)
print(mx * 10000)
