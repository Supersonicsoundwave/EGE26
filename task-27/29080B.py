from math import dist


def center(cl):
    res = []
    for dot in cl:
        sum_dist = sum(dist(dot, d) for d in cl)
        res += [(sum_dist, dot)]
    return min(res)[1]


with open(r'.\files\27_B_29080.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[0] == 'L':
            stars += [dots[-1]]

cl1 = [d for d in dots if 23 < d[1]]
cl2 = [d for d in dots if 16 < d[1] < 23]
cl3 = [d for d in dots if d[1] < 16]

st1 = [s for s in stars if 23 < s[1]]
st2 = [s for s in stars if 16 < s[1] < 23]
st3 = [s for s in stars if s[1] < 16]

cl_info = [[cl1, st1],
           [cl2, st2],
           [cl3, st3]]

cen_min = center(min(cl_info, key=lambda x: len(x[1]))[0])
cen_max = center(max(cl_info, key=lambda x: len(x[1]))[0])
B1 = dist(cen_min, cen_max)

B2 = []
for star1 in st1:
    for star2 in st2 + st3:
        B2.append(dist(star1, star2))
for star1 in st2:
    for star2 in st3:
        B2.append(dist(star1, star2))

print(B1 * 10_000, max(B2) * 10_000)
