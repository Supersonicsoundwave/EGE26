from math import dist
from itertools import combinations


with open(r'.\files\27_B_29081.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[1] >= '8':
            stars += [dots[-1]]

st1 = [s for s in stars if 23 < s[1]]
st2 = [s for s in stars if 16 < s[1] < 23]
st3 = [s for s in stars if s[1] < 16]

B1 = []
for star1 in st1:
    for star2 in st2 + st3:
        B1.append(dist(star1, star2))
for star1 in st2:
    for star2 in st3:
        B1.append(dist(star1, star2))

dist1 = [dist(s1, s2) for s1, s2 in combinations(st1, 2)]
dist2 = [dist(s1, s2) for s1, s2 in combinations(st2, 2)]
dist3 = [dist(s1, s2) for s1, s2 in combinations(st3, 2)]
sum_dists = dist1 + dist2 + dist3
B2 = sum(sum_dists) / len(sum_dists)

print(min(B1) * 10_000, B2 * 10_000)

######################################################################

from itertools import combinations
from math import dist

with open(r'.\files\27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append(list(map(float, [x, y])))
        if data[1] >= '8' and int(data[1]) >= 8 and data[1] in '89':
            stars.append(dots[-1])

stars_1 = [d for d in stars if 23 < d[1]]
stars_2 = [d for d in stars if 16 < d[1] < 23]
stars_3 = [d for d in stars if d[1] < 16]

B1 = []
for s1 in stars_1:
    for s2 in stars_2:
        B1.append(dist(s1, s2))
for s1 in stars_1:
    for s2 in stars_3:
        B1.append(dist(s1, s2))
for s1 in stars_2:
    for s2 in stars_3:
        B1.append(dist(s1, s2))
B1 = min(B1)

B2 = []
for s1 in stars_1:
    for s2 in stars_1:
        if s1 != s2:
            B2.append(dist(s1, s2))
for s1 in stars_2:
    for s2 in stars_2:
        if s1 != s2:
            B2.append(dist(s1, s2))
for s1 in stars_3:
    for s2 in stars_3:
        if s1 != s2:
            B2.append(dist(s1, s2))
B2 = sum(B2) / len(B2)
print(B1 * 10_000, B2 * 10_000)

##################################################

stars_1 = [d for d in stars if 23 < d[1]]
stars_2 = [d for d in stars if 16 < d[1] < 23]
stars_3 = [d for d in stars if d[1] < 16]
all_stars = [stars_1, stars_2, stars_3]

B1 = [dist(s1, s2) for cl1, cl2 in combinations(all_stars, 2) for s1 in cl1 for s2 in cl2]
B2 = [dist(s1, s2) for cl in all_stars for s1, s2 in combinations(cl, 2)]

print(min(B1) * 10_000, sum(B2) / len(B2) * 10_000)

##################################################

B1, B2 = [], []
for s1, s2 in combinations(stars, 2):
    u = sum(s1 in cl and s2 in cl for cl in all_stars)
    d = dist(s1, s2)
    if u: B2.append(d)
    else: B1.append(d)

print(min(B1) * 10_000, sum(B2) / len(B2) * 10_000)
