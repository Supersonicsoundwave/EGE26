with open(r'.\files\26_4629.txt') as file:
    N = int(file.readline())
    costs = sorted([int(i) for i in file])

amount_1 = sum(costs) - sum(costs[::-1][:N // 4]) // 2
amount_2 = sum(costs) - sum(costs[:N // 4]) // 2
print(amount_1, amount_2)
