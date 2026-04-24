def f(cur, end):
    if cur > end or cur == 7:
        return 0
    if cur == end:
        return 1
    return f(cur + 1, end) + f(cur + 3, end) + f(cur * 2, end)


print(f(2, 15) * f(15, 25))
