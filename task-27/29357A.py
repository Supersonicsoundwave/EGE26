from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_29357.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[0] == 'M' and data[2:] == 'III':
            stars += [list(map(float, (x, y)))]

cl1 = [d for d in dots if d[1] > 15]
cl2 = [d for d in dots if d[1] < 15]

min_cl = min(cl1, cl2, key=len)
min_cen = center(min_cl)

min_star = min(stars, key=lambda x: dist(x, min_cen))

Ax = min_star[0]
Ay = min_star[1]
print(Ax * 10_000, Ay * 10_000)
