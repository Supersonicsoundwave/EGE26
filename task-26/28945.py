with open(r'.\files\26_28945.txt') as file:
    data = [tuple(map(int, line.split())) for line in file]

ans = []
for i in range(len(data)):
    data[i] = (data[i][0], data[i][0] + data[i][1])

data = sorted(data, key=lambda x: (x[1], x[0]))
queue = [data[0]]
ost = []
for val in data[1:]:
    if val[0] >= queue[-1][-1]:
        queue += [val]

queue = queue[:-1]
for val in data[::-1]:
    if val[0] >= queue[-1][-1]:
        queue += [val]
        break

print(len(queue), 10_000 - queue[-1][-1])
