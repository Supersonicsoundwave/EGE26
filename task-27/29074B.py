from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_B_29074.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[0] == 'L' and data[2:] == 'V':
            stars += [list(map(float, (x, y)))]

cl1 = [[d for d in dots if d[1] > 23],
       [s for s in stars if s[1] > 23]]

cl2 = [[d for d in dots if 16 < d[1] < 23],
       [s for s in stars if 16 < s[1] < 23]]

cl3 = [[d for d in dots if d[1] < 16],
       [s for s in stars if s[1] < 16]]

cen1 = center(cl1[0])
cen2 = center(cl2[0])
cen3 = center(cl3[0])

min_dist2 = min(dist(cen2, star) for star in cl2[1])
min_dist3 = min(dist(cen3, star) for star in cl3[1])

B1 = min(min_dist2, min_dist3)

max_dist2 = max(dist(cen2, star) for star in cl2[1])
max_dist3 = max(dist(cen3, star) for star in cl3[1])

B2 = max(max_dist2, max_dist3)

print(B1 * 10_000, B2 * 10_000)
