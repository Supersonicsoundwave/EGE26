with open(r'.\files\26_1868.txt') as file:
    N = int(file.readline())
    places = [list(map(int, i.split())) for i in file]

dct = dict()
for row, place in places:
    if row not in dct:
        dct[row] = [place]
    else:
        dct[row] += [place]
        dct[row].sort()
ans = []
for row, seats in dct.items():
    for seat1, seat2 in zip(seats, seats[1:]):
        if seat2 - seat1 == 3:
            ans += [(row, seat1 + 1)]
print(*max(ans, key=lambda x: (x[0], -x[1])))

###########################################################

places = sorted(places, key=lambda x: (-x[0], x[1]))

for seat1, seat2 in zip(places, places[1:]):
    if seat1[0] == seat2[0]:
        if seat2[1] - seat1[1] == 3:
            print(seat1[0], seat1[1] + 1)
            break



