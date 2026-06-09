with open(r'files/26_4660.txt') as file:
    N = int(file.readline())
    costs = [int(i) for i in file]

costs = sorted(costs)

price_1 = sum(costs) - sum(costs[::-1][3::4]) // 2
price_2 = sum(costs) - sum(costs[:N // 4]) // 2
print(price_1, price_2)
