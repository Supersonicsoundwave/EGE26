def f(cur, end):
    if cur > end:
        return 0
    if cur == end:
        return 1
    return f(cur + 1, end) + f(cur + 2, end) + f(cur + 3, end)


print(f(5, 7) * f(7, 11))
