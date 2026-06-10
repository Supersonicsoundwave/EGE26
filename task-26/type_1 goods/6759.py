with open(r'.\files\26_6759.txt') as file:
    N = int(file.readline())
    costs = [int(i) for i in file]

costs.sort(reverse=True)
price_1 = sum(costs) - sum(costs[:N // 3])
price_2 = sum(costs) - sum(costs[2::3])
print(price_1, price_2)
