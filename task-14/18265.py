for p in range(30, 37):
    for s in range(10, 35):
        a = int('r4', p - 1)
        b = int('b0', s + 2)
        c = int('t3nk4', p)
        if a + b + c == 23593399:
            print(p * s)