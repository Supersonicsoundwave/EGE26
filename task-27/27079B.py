with open(r'.\files\27_B_29079.txt') as file:
    dots = []
    stars = []
    for line in file:
        x, y, data = line.replace(',', '.').split()
        dots += [list(map(float, (x, y)))]
        if data[0] == 'J' and data[2:] == 'V':
            stars += [dots[-1]]

cl1 = [[d for d in dots if 23 < d[1]],
       [s for s in stars if 23 < s[1]]]
cl2 = [[d for d in dots if 16 < d[1] < 23],
       [s for s in stars if 16 < s[1] < 23]]
cl3 = [[d for d in dots if d[1] < 16],
       [s for s in stars if s[1] < 16]]

max_cl_st = max(cl1, cl2, cl3, key=lambda x: len(x[0]))[1]
B1 = max(max_cl_st, key=lambda x: x[0])[0]

min_cl_st = min(cl1, cl2, cl3, key=lambda x: len(x[0]))[1]
B2 = max(min_cl_st, key=lambda x: x[1])[1]

print(B1 * 10_000, B2 * 10_000)
