with open(r'.\files\17628.txt') as file:
    data = [list(map(int, line.split())) for line in file]

cnt = 0
for line in data:
    line = sorted(line)
    if line[0] + line[-1] <= sum(line[1:3]):
        cnt += 1
print(cnt)

