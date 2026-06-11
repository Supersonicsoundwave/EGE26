with open(r'.\files\26_17687.txt') as file:
    N = int(file.readline())
    costs = [int(i) for i in file]

costs.sort(reverse=True)
price1 = sum(costs) - sum(costs[:N//9])
price2 = sum(costs) - sum(costs[8::9])
print(price1, price2)
