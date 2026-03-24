with open(r'.\files\17550.txt') as file:
    data = [list(map(int, line.split())) for line in file]

cnt = 0
for line in data:
    amount = [line.count(num) for num in set(line)]
    if sorted(amount) == [1, 1, 1, 3]:
        dub = [num for num in line if line.count(num) != 1]
        not_dub = [num for num in line if line.count(num) == 1]
        if sum(dub) ** 2 > sum(not_dub) ** 2:
            cnt += 1
print(cnt)
