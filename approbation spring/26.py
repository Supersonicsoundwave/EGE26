def maxline(numbers):
    lines = []
    line = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] - line[-1] == 1:
            line += [numbers[i]]
        else:
            lines += [line]
            line = [numbers[i]]
    lines += [line]
    return len(max(lines, key=len))


with open(r'.\files\26.txt') as file:
    c = file.readline()
    data = [tuple(map(int, line.split())) for line in file]

dct = {}
for line in data:
    number, spot = line
    if spot not in dct:
        dct[spot] = [number]
    else:
        dct[spot] += [number]
        dct[spot]= sorted(set(dct[spot]))

ans = []
for spot, numbers in dct.items():
    ans += [(maxline(numbers), spot)]

print(*max(ans, key=lambda tpl: (tpl[0], -tpl[1])))

