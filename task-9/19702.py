from itertools import combinations


with open(r'.\files\19702.txt') as file:
    data = [list(map(int, line.split())) for line in file]

cnt = 0
for line in data:
    line = sorted(line)
    for a1, a2, a3, a4 in combinations(line, r=4):
        if a4 - a3 == a3 - a2 == a2 - a1 != 0:
            cnt += 1
            break

print(cnt)
