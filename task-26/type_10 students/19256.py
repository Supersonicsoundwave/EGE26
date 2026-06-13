with open(r'.\files\26_19256.txt') as file:
    N = int(file.readline())
    data = dict()
    for i in range(N):
        ID, task = map(int, file.readline().split())
        if ID not in data:
            data[ID] = {task}
        else:
            data[ID] |= {task}

ans = []
for ID in data:
    tasks = sorted(data[ID])
    cnt = 1
    for i in range(len(tasks) - 1):
        if tasks[i + 1] - tasks[i] == 1:
            cnt += 1
        else:
            cnt = 1
        ans += [(cnt, ID)]
print(*max(ans, key=lambda x: (x[0], -x[1]))[::-1])
