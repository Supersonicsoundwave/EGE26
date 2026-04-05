from turtle import *


with open(r'.\files\27_A.txt') as file:
    data = [tuple(map(float, line.replace(',', '.').split())) for line in file]


KL = [[], []]
for x, y in data:
    if y < 15:
        KL[0] += [(x, y)]
    else:
        KL[1] += [(x, y)]

# tracer(False)
# screensize(3000, 3000)
# m = 15
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


print(len(min(KL, key=len)))
centers = [center(kl) for kl in KL]
print(int(sum(dist(x, y, -1,1.3) for x, y in centers) * 10_000))
print(centers)


