from string import printable as alph


for x in alph[:19][::-1]:
    a = int(f'98{x}79641', 19)
    b = int(f'36{x}14', 19)
    c = int(f'73{x}4', 19)
    f = a + b + c
    if f % 18 == 0:
        print(f // 18)
        break