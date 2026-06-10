with open(r'.\files\26_9793.txt') as file:
    N = int(file.readline())
    times = []
    for i in range(1, N + 1):
        grind, paint = [int(i) for i in file.readline().split()]
        if paint < grind:
            times += [(paint, i, 'p')]
        else:
            times += [(grind, i, 'g')]

times.sort(key=lambda x: x[0])
cnt = sum(1 for time in times if time[2] == 'g')
if times[-1][2] == 'g':
    cnt -= 1
print(times[-1][1], cnt)


