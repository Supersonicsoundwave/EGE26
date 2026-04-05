def f(cur, end):
    if cur < end or cur == 7:
        return 0
    if cur == end:
        return 1
    return f(cur - 1, end) + f(cur - 4, end) + f(cur // 3, end)


print(f(19, 13) * f(13, 2))
