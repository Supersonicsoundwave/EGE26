from string import printable


for x in printable[:25]:
    a = int(f'11353{x}12', 25)
    b = int(f'135{x}21', 25)
    f = a + b
    if f % 24 == 0:
        print(f // 24)
