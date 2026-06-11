with open(r'.\files\26_6056.txt') as file:
    N = int(file.readline())
    rings = [int(i) for i in file]

rings.sort(reverse=True)
order = [rings[0]]
for ring in rings[1:]:
    if order[-1] - ring >= 56:
        order += [ring]
print(len(order), min(order))
