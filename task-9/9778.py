with open(r'.\files\09_9778.csv') as file:
    data = [[int(num) for num in line.rstrip().split(';')] for line in file.readlines()]

for pos, line in enumerate(data, start=1):
    amount = [line.count(num) for num in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 2]:
        dub = [num for num in set(line) if line.count(num) == 2][0]
        not_dub = [num for num in line if line.count(num) == 1]
        if dub >= sum(not_dub) / 4:
            print(pos)
            break


