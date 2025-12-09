from string import printable


for x in printable[1:35]:
    a = int(f'6{x}qr{x}', 35)
    b = int(f'{x}59sh', 35)
    c = int(f'ph{x}69yw', 35)
    f = a + b + c
    repeat = int(max(str(f), key=lambda x: (str(f).count(x), int(x)))) ** 2
    if f % repeat == 0:
        print(f // repeat)
