for p in range(36, 10, -1):
    a = int('29A1', p)
    b = int('47771', p)
    c = int('12A', p)
    f = a + b + c
    if f > 1_000_000:
        for x in range(1, 500_000):
            if f == 1_000_000 + x:
                print(p)
