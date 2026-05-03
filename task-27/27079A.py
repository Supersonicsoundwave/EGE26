from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_A_29079.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[2:] == 'IV' and data[0] == 'N':
            stars += [dots[-1]]

cl1 = [d for d in dots if d[1] < 8]
cl2 = [d for d in dots if d[1] > 8]

st1 = [s for s in stars if s[1] < 8]
st2 = [s for s in stars if s[1] > 8]

cen1 = center(cl1)
cen2 = center(cl2)

A1 = min(min(dist(cen1, s) for s in st2), min(dist(cen2, s) for s in st1))

A2 = max(max(dist(cen1, s) for s in st2), max(dist(cen2, s) for s in st1))

print(A1 * 10_000, A2 * 10_000)
