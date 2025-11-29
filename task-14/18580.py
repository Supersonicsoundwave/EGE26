from string import printable


for x in printable[:25]:
    a = int(f'a4{x}7f2', 25)
    b = int(f'n{x}g5{x}h', 25)
    c = int(f'74{x}m26', 25)
    f = a + b + c
    if f % 24 == 0:
        print(f // 24)