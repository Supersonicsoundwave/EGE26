from string import printable


for x in printable[:23]:
    a = int(f'7{x}38596', 23)
    b = int(f'14{x}36', 23)
    c = int(f'61{x}7', 23)
    f = a + b + c
    if f % 22 == 0:
        print(f // 22)
        break