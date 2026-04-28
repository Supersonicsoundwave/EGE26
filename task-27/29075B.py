from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_B_29075.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if 'J' in data:
            stars += [list(map(float, (x, y)))]

cl1 = [s for s in stars if s[1] > 22]

cl2 = [s for s in stars if s[1] < 22 and s[0] < 22]

cl3  = [s for s in stars if s[0] > 22]

B1 = 10**20
B2 = 0

for star1 in cl1:
    for star2 in cl2 + cl3:
        dst = dist(star1, star2)
        B1 = min(B1, dst)
        B2 = max(B2, dst)

for star1 in cl2:
    for star2 in cl3:
        dst = dist(star1, star2)
        B1 = min(B1, dst)
        B2 = max(B2, dst)

print(B1 * 10_000, B2 * 10_000)
