with open(r'.\files\26_23283.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, line.split())) for line in file]

times.sort()
windows = [0] * K

cnt = 0
last_window = 0

for person in times:
    for i in range(K):
        if windows[i] < person[0]:
            windows[i] = person[1]
            cnt += 1
            last_window = i + 1
            break
print(cnt, last_window)
