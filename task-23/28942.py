def f(cur, end):
    if cur < end or cur == 73:
        return 0
    if cur == end:
        return 1
    return f(cur - 3, end) + f(cur - 8, end) + f(cur // 2, end)


print(f(76, 41) * f(41, 12))
