with open(r'.\files\9_20219.csv') as file:
    data = [line.rstrip() for line in file.readlines()]

cnt = 0
for line in data:
    a1, a2, a3, a4, a5, a6 = line.split(',')
    cond1 = (len(a1) == 3) + (len(a2) == 3) + (len(a3) == 3) + (len(a4) == 3) + (len(a5) == 3) + (len(a6) == 3)
    cond2 = (int(a1) % 5 == 0) + (int(a2) % 5 == 0) + (int(a3) % 5 == 0) + (int(a4) % 5 == 0) + \
            (int(a5) % 5 == 0) + (int(a6) % 5 == 0)
    if cond1 >= 3 and cond2 == 0:
        cnt += 1
print(cnt)
