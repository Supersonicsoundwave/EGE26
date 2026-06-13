with open(r'.\files\26_23383.txt') as file:
    N = int(file.readline())
    points = dict()
    for line in file:
        ID, point = map(int, line.split())
        if point not in points:
            points[point] = {ID}
        else:
            points[point] |= {ID}

ans = []
for point in points:
    sportsmen = sorted(points[point])
    cnt = 1
    for i in range(len(sportsmen) - 1):
        if sportsmen[i + 1] - sportsmen[i] == 1:
            cnt += 1
        else:
            cnt = 1
        ans += [(cnt, point)]
print(*max(ans, key=lambda x: (x[0], -x[1])))
