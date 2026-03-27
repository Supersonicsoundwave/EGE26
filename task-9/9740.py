with open(r'.\files\9740.txt') as file:
    data = [list(map(int, line.split())) for line in file]

cnt = 0
for line in data:
    amount = [line.count(num) for num in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 3]:
        not_dub = [num for num in line if line.count(num) == 1]
        dub = [num for num in set(line) if line.count(num) == 3][0]
        if sum(not_dub) / len(not_dub) <= dub:
            cnt += 1
print(cnt)
