for p in range(int(max('BOOMBLCNG'), 36) + 1, 37):
    a = int('BO', p)
    b = int('OM', p)
    c = int('BL4', p)
    d = int('CNG', p)
    if a + b + c == d:
        print(p)


