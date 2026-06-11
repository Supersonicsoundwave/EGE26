with open(r'.\files\26_17537.txt') as file:
    N, M, K = map(int, file.readline().split())
    places = [list(map(int, line.split())) for line in file]

seats = [M] * (K + 1)
for row, seat in places:
    seats[seat] = min(seats[seat], row - 1)

ans = []
for i in range(1, K + 1 - 1):
    ans.append([min(seats[i], seats[i + 1]), i + 1])

print(*max(ans))

# ans = 0
# for seat1, seat2 in zip(seats, seats[1:]):
#     ans = max(ans, min(seat1, seat2))
#
# print(ans, seats.index(ans) + 1)

