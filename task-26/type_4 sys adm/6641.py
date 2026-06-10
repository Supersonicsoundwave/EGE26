with open(r'.\files\26_6641.txt') as file:
    N, M = list(map(int, file.readline().split()))
    costs = []
    for line in file:
        price, info = line.split()
        costs += [[int(price), 1 if info == 'W' else 0]]

costs = sorted(costs)

cnt_S = 0
bought = []
sm = 0
for cost in costs:
    if sm + cost[0] <= M:
        sm += cost[0]
        bought += [cost]
        cnt_S += 1 if cost[1] == 0 else 0

ln = len(bought)
for cost1 in bought[::-1]:
    if cost1[1] == 1:
        for cost2 in costs[ln:]:
            ln += 1
            if cost2[1] == 0:
                if sm - cost1[0] + cost2[0] <= M:
                    bought.remove(cost1)
                    bought += [cost2]
                    cnt_S += 1
                    sm += - cost1[0] + cost2[0]
                    break
print(cnt_S, M - sm)
