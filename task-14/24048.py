def conv10(x, q):
    x = x[::-1]
    res = 0
    for i in range(len(x)):
        res += int(x[i], 36) * q ** i
    return res


for p in range(34, 100):
    cat = conv10('KOT', p)
    hungry = conv10('GOLODNI', p)
    meow = conv10('MEEOW', p)
    a = conv10('100', p)
    if cat + hungry == meow * a - 20194023088:
        print(conv10('PURR', p))
        break
