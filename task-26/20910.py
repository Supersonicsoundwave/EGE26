with open(r'.\files\26_20910.txt') as file:
    N, M, K = list(map(int, file.readline().split()))
    places = [list(map(int, i.split())) for i in file]

places.sort(key=lambda x: (-x[0], x[1]))
hall = dict()
for place in places:
    if place[0] not in hall:
        hall[place[0]] = [place[1]]
    else:
        hall[place[0]] += [place[1]]
        hall[place[0]].sort()

rows = list(hall.keys())
for i in range(len(rows)):
    for seat1, seat2 in zip(range(1, K + 1), range(2, K + 1)):
        if all(seat1 not in hall[r] and seat2 not in hall[r] for r in rows[i:]):
            print(rows[i], seat1)
