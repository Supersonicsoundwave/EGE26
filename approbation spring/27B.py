from turtle import *


with open(r'.\files\27_B.txt') as file:
    data = [tuple(map(float, line.replace(',', '.').split())) for line in file]


KL = [[], [], []]
for x, y in data:
    if y > 22:
        KL[0] += [(x, y)]
    elif x < 24:
        KL[1] += [(x, y)]
    else:
        KL[2] += [(x, y)]

# tracer(False)
# screensize(3000, 3000)
# m = 20
# colors = ['red', 'green', 'blue']
# up()
# for i in range(len(KL)):
#     for x, y in KL[i]:
#         goto(x * m, y * m)
#         dot(3,colors[i])
# update()
# done()


def dist(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


def sumdist(x1, y1, kl):
    return sum(dist(x1, y1, x2, y2) for x2, y2 in kl)


def center(kl):
    minsumdist = 10 ** 20
    for x1, y1 in kl:
        if sumdist(x1, y1, kl) < minsumdist:
            minsumdist = sumdist(x1, y1, kl)
            x, y = x1, y1
    return x, y


xc1, yc1 = center(KL[1])
print(sum(1 for x, y in KL[1] if dist(x, y, xc1, yc1) <= 1.6) - 1)

xc0, yc0 = center(KL[0])
print(int(max(dist(x, y, xc0, yc0) for x, y in KL[0]) * 10_000))

