with open(r'.\files\7030.txt') as file:
    data = [list(map(int, line.split())) for line in file]

cnt = 0
for line in data:
    amount = [line.count(num) for num in set(line)]
    if sorted(amount) == [2, 2, 2]:
        a, b, c = sorted(set(line))
        if a ** 2 + b ** 2 == c ** 2:
            cnt += 1
print(cnt)
