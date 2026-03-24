def conv10(lst, q):
    lst = lst[::-1]
    res = 0
    for i in range(len(lst)):
        res += lst[i] * q ** i
    return res


for x in range(37):
    a = conv10([9, 8, x, 3, 1], 37)
    b = conv10([1, x, 9, 2, 4], 37)
    f = a + b
    if f % 21 == 0:
        print(f // 21)
