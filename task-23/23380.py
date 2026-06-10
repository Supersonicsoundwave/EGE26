def f(cur, end):
    if cur > end or cur ==10:
        return 0
    if cur == end:
        return 1
    return f(cur + 1, end) + f(cur + 2, end) + f(cur * 2, end)


print(f(3, 7) * f(7, 20))
