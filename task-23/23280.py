def f(cur, end):
    if cur == end:
        return 1
    if cur < end or cur == 8:
        return 0
    return f(cur - 1, end) + f(cur - 4, end) + f(cur // 3, end)


print(f(19, 14) * f(14, 2))
