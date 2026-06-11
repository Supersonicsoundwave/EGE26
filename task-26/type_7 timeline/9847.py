with open(r'.\files\26_9847.txt') as file:
    N = int(file.readline())
    visitors = [list(map(int, line.split())) for line in file]

timeline = [0] * 1440
for start, end in visitors:
    for i in range(start, end):
        timeline[i] += 1

ans = []
for i in range(1440):
    if timeline[i] == max(timeline):
        ans += [i]

cnt = 1
for n1, n2 in zip(ans, ans[1:]):
    if n2 - n1 > 1:
        cnt += 1

print(cnt, max(timeline))
