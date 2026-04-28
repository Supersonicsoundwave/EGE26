from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_B_29076.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if 'Y' in data:
            stars += [list(map(float, (x, y)))]

cl1 = [[d for d in dots if d[1] > 24],
       [s for s in stars if s[1] > 24]]

cl2 = [[d for d in dots if d[1] < 24 and d[0] < 20],
       [s for s in stars if s[1] < 24 and s[0] < 20]]

cl3 = [[d for d in dots if d[0] > 24],
       [s for s in stars if s[0] > 24]]

cls = [cl1, cl2, cl3]

max_cl = max(cls, key=lambda x: len(x[1]))[0]
min_cl = min(cls, key=lambda x: len(x[1]))[0]
B1 = dist(center(min_cl), center(max_cl))

B2 = 0
for cl in cls:
    cen = center(cl[0])
    max_dist = max(dist(cen, star) for star in cl[1])
    B2 = max(B2, max_dist)

print(B1 * 10_000, B2 * 10_000)
