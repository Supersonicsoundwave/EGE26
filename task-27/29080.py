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
        if 'L3' in data:
            stars += [dots[-1]]

cl1 = [d for d in dots if d[1] > 10]
cl2 = [d for d in dots if d[1] < 10]
min_cl_cen = center(min(cl1, cl2, key=len))
max_cl_cen = center(max(cl1, cl2, key=len))

A1 = max(dist(min_cl_cen, s) for s in stars)
A2 = max(dist(max_cl_cen, s) for s in stars)


with open(r'.\files\27_B_29080.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if 'L' in data:
            stars += [dots[-1]]

cl1 = [[d for d in dots if d[1] > 22],
       [s for s in stars if s[1] > 22]]
cl2 = [[d for d in dots if 22 > d[1] > 16],
       [s for s in stars if 22 > s[1] > 16]]
cl3 = [[d for d in dots if d[1] < 16],
       [d for d in stars if d[1] < 16]]

min_cl = center(min(cl1, cl2, cl3, key=lambda x: len(x[1]))[0])
max_cl = center(max(cl1, cl2, cl3, key=lambda x: len(x[1]))[0])

B1 = dist(min_cl, max_cl)

ans = []
for s1 in cl1[1] + cl2[1]:
    for s2 in cl3[1]:
        ans += [dist(s1, s2)]
for s1 in cl1[1]:
    for s2 in cl2[1]:
        ans += [dist(s1, s2)]

B2 = max(ans)

print(A1 * 10_000, A2 * 10_000)
print(B1 * 10_000, B2 * 10_000)
