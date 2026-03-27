with open(r'.\files\23193.txt') as file:
    data = [list(map(int, line.split())) for line in file]


for pos, line in enumerate(data, start=1):
    amount = [line.count(num) for num in set(line)]
    if sorted(amount) == [1, 1, 1, 3]:
        not_dub = [num for num in line if line.count(num) ==  1]
        dub = [num for num in line if line.count(num) != 1][0]
        if dub > sum(not_dub) / len(not_dub):
            print(pos)
