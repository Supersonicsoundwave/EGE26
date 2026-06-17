with open(r'.\files\27764.txt') as file:
    data = [list(map(int, line.split())) for line in file]

cnt = 0
for line in data:
    if len(line) == len(set(line)):
        line = sorted(line)
        if 2 * (line[0] + line[-1]) == sum(line) - min(line) - max(line):
            cnt += 1
print(cnt)
