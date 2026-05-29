with open(r'.\files\26_23283.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times)
windows = [0] * K

cnt = 0
last = 0
for time in times:
    for i in range(K):
        if time[0] > windows[i]:
            windows[i] = time[1]
            cnt += 1
            last = i + 1
            break
print(cnt, last)
