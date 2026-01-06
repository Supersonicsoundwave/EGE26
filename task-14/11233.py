from string import printable


for x in printable[:26]:
    a = int(f'27{x}98876', 26)
    b = int(f'26{x}51', 26)
    c = int(f'15{x}47', 26)
    d = int(f'62{x}5', 26)
    f = a + b + c + d
    if f % 25 == 0:
        print(f // 25)