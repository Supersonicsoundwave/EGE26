with open(r'.\files\24346.txt') as file:
    data = [list(map(int, line.split())) for line in file]

for pos, line in enumerate(data, start=1):
    if len(line) != len(set(line)):
        dub = [num for num in line if line.count(num) != 1]
        not_dub = [num for num in line if line.count(num) == 1]
        if sum(dub) ** 2 > sum(not_dub) ** 2:
            if sum(line) % 2 != 0:
                print(pos)
