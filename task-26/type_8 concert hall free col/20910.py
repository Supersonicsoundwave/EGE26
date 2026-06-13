with open(r'.\files\26_20910.txt') as file:
    N, M, K = map(int, file.readline().split())
    places = [list(map(int, line.split())) for line in file]

hall = [M] * (K + 1)
for row, seat in places:
    hall[seat] = min(row - 1, hall[seat])

ans = []
for i in range(1, K + 1 - 1):
    ans += [(min(hall[i], hall[i + 1]), i)]
print(*min(ans, key=lambda x: (-x[0], x[1])))
