with open(r'.\files\26_17643.txt') as file:
    data = [tuple(map(int, line.split())) for line in file]

mid_cost = sum([line[1] for line in data])/len([line[1] for line in data])
pricey = dict()
for line in data:
    art, cost, x = line
    if cost > mid_cost:
        if art not in pricey:
            pricey[art] = [cost, int(not x), cost * (not x), x]
        else:
            pricey[art] = [cost, pricey[art][1] + (not x), pricey[art][2] + cost * (not x), pricey[art][3] + x]

ans = max(pricey.values(), key=lambda x: (x[1], x[0], -x[3]))
print(ans)
