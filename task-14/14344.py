for p in range(16, 37):
    a = int('17496', p)
    b = int('91f83', p)
    c = int('d9543', p)
    f = a + b + c
    if f % 12 == 0:
        print(f // 12)