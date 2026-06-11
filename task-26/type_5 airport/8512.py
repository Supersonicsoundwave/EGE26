with open(r'.\files\26_8512.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    times = [list(map(int, line.split())) for line in file]

times.sort()
cells = [0] * K

cnt = 0
last_cell = 0
for person in times:
    for i in range(K):
        if cells[i] < person[0]:
            cells[i] = person[1]
            cnt += 1
            last_cell = i + 1
            break

print(cnt, last_cell)
