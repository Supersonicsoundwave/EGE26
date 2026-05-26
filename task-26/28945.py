with open(r'.\files\26_28945.txt') as file:
    data = [tuple(map(int, line.split())) for line in file]

# неверно
ans = []
for i in range(len(data)):
    data[i] = (data[i][0], data[i][0] + data[i][1])

data = sorted(data, key=lambda x: x[0])
for i in range(100):
    queue = [data[1]]
    for val in data:
        if val[0] >= queue[-1][-1]:
            queue += [val]
    ans += [(len(queue), 10_000 - queue[-1][-1])]

print(max(ans, key=lambda x: (x[0], -x[1])))
