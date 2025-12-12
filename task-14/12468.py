from string import printable


for x in printable[:19]:
    a = int(f'78{x}79643', 19)
    b = int(f'25{x}43', 19)
    c = int(f'63{x}5', 19)
    f = a + b + c
    if f % 18 == 0:
        print(f // 18)

