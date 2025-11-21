from string import printable

ans = []
for y in range(9, 13):
    for x in range(y + 1, 14):
        a = int(f'7{printable[x]}37{printable[y]}', 14)
        b = int(f'9{printable[y]}63', x)
        c = int(f'15148', y)
        f = a + b - c
        ans += [(f, f // (x + y))]
print(max(ans))
