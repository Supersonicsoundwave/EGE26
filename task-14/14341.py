from string import printable


for x in printable[:22]:
    a = int(f'56{x}c20', 22)
    b = int(f'89f{x}2', 22)
    c = int(f'h24{x}k21', 22)
    f = a + b + c
    if f % 21 == 0:
        print(f // 21)
