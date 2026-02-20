def f(cur, end):
    if cur == end:
        return 1
    if cur < end or cur in [9, 16]:
        return 0
    return f(cur - 1, end) + f(cur - 2, end) + f(cur // 3, end)


print(f(19, 3))
