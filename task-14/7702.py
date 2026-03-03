from string import printable


ans = set()
for y in printable[9:18]:
    for x in printable[:int(y, 36)]:
        f = int(f'5{x}{y}A', 18) + int(f'18{x}7', int(y, 36))
        ans |= {f}
print(len(ans))
