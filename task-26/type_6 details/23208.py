with open(r'.\files\26_23208.txt') as file:
    N = int(file.readline())
    details = []
    for pos, line in enumerate(file, start=1):
        grind, paint = map(int, line.split())
        if grind < paint:
            details += [(grind, pos, 'g')]
        else:
            details += [(paint, pos, 'p')]

details.sort(key=lambda x: x[0])
ans1 = details[-1][1]
ans2 = sum(detail[2] == 'g' for detail in details[:-1])
print(ans1, ans2)
