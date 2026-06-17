with open(r'.\files\29962.txt') as file:
    data = [list(map(int, line.split())) for line in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 3]:
        dub = [i for i in line if line.count(i) != 1]
        not_dub = [i for i in line if line.count(i) == 1]
        if sum(not_dub) / len(not_dub) > dub[0]:
            print(pos)
