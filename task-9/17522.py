with open(r'.\files\17522.txt') as file:
    data = [list(map(int, line.split())) for line in file]

cnt = 0
for line in data:
    line = sorted(line)
    if line[-1] < sum(line[:-1]):
        if len(set(line)) == 3:
            cnt += 1

print(cnt)
