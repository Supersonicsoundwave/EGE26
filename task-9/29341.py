with open(r'.\files\29341.txt') as file:
    data = [list(map(int, line.split())) for line in file]

cnt = 0
for line in data:
    if max(line) < sum(line) - max(line):
        line.sort()
        if line[0] + line[-1] != line[1] + line[2]:
            cnt += 1
print(cnt)
