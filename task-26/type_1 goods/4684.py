with open(r'.\files\26_4684.txt') as file:
    N = int(file.readline())
    costs = sorted([int(i) for i in file])

amount_1 = sum(costs) - sum(costs[::-1][5::6]) // 2
amount_2 = sum(costs) - sum(costs[:N // 6]) // 2
print(amount_1, amount_2)
