with open(r'.\files\26_6031.txt') as file:
    N = int(file.readline())
    rings = [int(i) for i in file]

rings.sort(reverse=True)
order = [rings[0]]
for ring in rings[1:]:
    if ring + 6 <= order[-1]:
        order += [ring]
print(len(order), order[-1])
