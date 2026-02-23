def f(cur, end):
    if cur < end:
        return 0
    if cur == end:
        return 1
    return f(cur - 1, end) + f(cur // 2, end)


print(f(30, 8) * f(8, 1))
