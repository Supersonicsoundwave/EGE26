with open(r'.\files\24347.txt') as file:
    data = [list(map(int, line.split())) for line in file]


cnt = 0
for line in data:
    cond1 = line.count(max(line)) == 1
    cond2 = line[0] not in [min(line), max(line)] and line[-1] not in [min(line), max(line)]
    line = sorted(line)
    cond3 = (line[-1] * line[-2] * line[-3]) % line[0] == 0
    if sum((cond1, cond2, cond3)) == 1:
        cnt += 1
print(cnt)
