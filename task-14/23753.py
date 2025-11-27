from string import printable


for x in printable[:29]:
    a = int(f'923{x}874', 29)
    b = int(f'524{x}6152', 29)
    f = a + b
    if f % 28 == 0:
        print(f // 28)