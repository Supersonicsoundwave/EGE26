from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_28766.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[0] == 'Y' and data[2:] == 'III':
            stars += [list(map(float, (x, y)))]

cl1 = [d for d in dots if d[1] > 8]
cl2 = [d for d in dots if d[1] < 8]
cls = [cl1, cl2]
min_cen = center(min(cls, key=len))
print(min(dist(min_cen, d) for d in stars) * 10_000)
print(max(dist(min_cen, d) for d in stars) * 10_000)
