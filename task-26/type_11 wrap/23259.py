with open(r'.\files\26_15_23259.txt') as file:
    N, M = map(int, file.readline().split())
    crews = []
    sleds = []
    for i in range(N):
        crews += [int(file.readline())]
    for i in range(M):
        sleds += [int(file.readline())]

crews.sort()
sleds.sort()

approved = []
last_sled = 0
for crew in crews:
    for sled in sleds:
        if sled >= crew:
            approved += [crew]
            last_sled = sled
            sleds.remove(sled)
            break

approved = approved[:-1]
for crew in crews[::-1]:
    if crew <= last_sled:
        approved += [crew]
        break
print(len(approved), max(approved))
