with open(r'.\files\23268.txt') as file:
    data = [list(map(int, line.split())) for line in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(num) for num in set(line)]
    if sorted(amount) == [1, 1, 1, 2, 2]:
        dub = [num for num in line if line.count(num) != 1]
        not_dub = [num for num in line if line.count(num) == 1]
        if sum(dub) / len(dub) < max(not_dub):
            print(pos)
            break
