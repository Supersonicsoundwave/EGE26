for p in range(int(max('thnqul'), 36) + 1, 37):
    a = int('th', p)
    b = int('nq', p)
    c = int('u', p)
    d = int('1l7', p)
    if a + b + c == d:
        print(p)
