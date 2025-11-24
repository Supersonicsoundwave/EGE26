from string import printable

for x in printable[1:13]:
    a = int(f'9{x}AB', 13)
    b = int(f'{x}46C', 16)
    c = int(f'B7{x}', 15)
    f = a + b - c
    if f % 14 == 0:
        print(f // 14)