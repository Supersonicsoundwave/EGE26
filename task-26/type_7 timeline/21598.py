with open(r'.\files\26_21598.txt') as file:
    N = int(file.readline())
    times = [list(map(int, line.split())) for line in file]

timeline = [0] * (1440 + 1)
for time in times:
    for i in range(time[0], time[1] + 1):
        timeline[i] += 1

cnt = 0
ans1 = []
ans2 = 0
for i in range(1, 1440 + 1 - 1):
    if timeline[i - 1] == timeline[i] == timeline[i + 1] != 0:
        cnt += 1
    elif timeline[i] != timeline[i + 1]:
        cnt = 0
        ans1 += [i]
    ans2 = max(ans2, cnt)

print(ans1[-2], ans2)
