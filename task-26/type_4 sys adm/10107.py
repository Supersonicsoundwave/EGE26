with open(r'.\files\26_10107.txt') as file:
    N = int(file.readline())
    events = [list(map(int, line.split())) for line in file]

events.sort(key=lambda x: (x[1], x[0]))
order = [events[0]]
for event in events[1:]:
    if event[0] >= order[-1][1]:
        order += [event]

order = order[:-1]
for event in events[::-1]:
    if event[0] >= order[-1][1]:
        order += [event]
        break

print(len(order), order[-1][0] - order[-2][1])
