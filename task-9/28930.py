with open(r'.\files\28930.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    sorted_line = sorted(line)
    if line == sorted_line and len(line) == len(set(line)):
        if min(line) + max(line) <= sum(line) - min(line) - max(line):
            cnt += 1
print(cnt)
