from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_29080.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[:2] == 'L3':
            stars += [dots[-1]]

cl1 = [d for d in dots if d[1] < 8]
cl2 = [d for d in dots if d[1] > 8]

cen_min = center(min(cl1, cl2, key=len))
cen_max = center(max(cl1, cl2, key=len))

A1 = max(dist(cen_min, s) for s in stars)
A2 = max(dist(cen_max, s) for s in stars)

print(A1 * 10_000, A2 * 10_000)
