from string import printable


for x in printable[:22]:
    a  = int(f'a23{x}ac0', 22)
    b = int(f'gb{x}21670', 22)
    f = a + b
    if f % 21 == 0:
        print(f // 22)