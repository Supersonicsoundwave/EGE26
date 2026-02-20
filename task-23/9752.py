def f(cur, end):
    if cur == end:
        return 1
    if cur > end or cur == 17:
        return 0
    return f(cur + 2, end) + f(cur + 3, end) + f(cur * 2, end)


print(f(3, 10) * f(10, 25))
