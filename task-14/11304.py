from string import printable

for x in printable[:16]:
    a = int(f'11{x}73', 16)
    b = int(f'94662{x}53{x}', 16)
    c = int(f'6{x}41', 16)
    d = int(f'31{x}77', 16)
    e = int(f'9{x}82{x}{x}181', 16)
    f = a + b + c + d + e
    if f % 15 == 0:
        print(f // 15)