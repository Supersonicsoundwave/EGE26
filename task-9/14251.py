with open(r'.\files\14251.txt') as file:
    data = [list(map(int, line.split())) for line in file]

for line in data:
    amount = [line.count(num) for num in set(line)]
    if sorted(amount) == [1, 1, 1, 2, 2]:
        dub = [num for num in line if line.count(num) != 1]
        chet = [num for num in line if num % 2 != 0]
        if sum(dub) <= sum(chet):
            print(sum(line))
            break

