from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_29075.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[2:] == 'III':
            stars += [list(map(float, (x, y)))]

cl1 = [[d for d in dots if d[1] > 10],
       [s for s in stars if s[1] > 10]]

cl2 = [[d for d in dots if d[1] < 10],
       [s for s in stars if s[1] < 10]]

cls = [cl1, cl2]

A1 = center(min(cls, key=lambda x: len(x[1]))[0])[0]
A2 = center(max(cls, key=lambda x: len(x[1]))[0])[1]

print(A1 * 10_000, A2 * 10_000)