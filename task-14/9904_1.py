from string import printable


ans = []
for y in printable[9:14]:
    for x in printable[int(y, 36) + 1:14]:
        a = int(f'7{x}37{y}', 14)
        b = int(f'9{y}63', int(x, 36))
        c = int('15148', int(y, 36))
        f = a + b - c
        ans += [(f, f // (int(x, 36) + int(y, 36)))]
print(max(ans))

