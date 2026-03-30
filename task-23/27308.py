def f(cur, end):
    if cur < end:
        return 0
    if cur == end:
        return 1
    return f(cur - 3, end) + f(cur - 5, end) + f(cur // 3, end)


print(f(80, 18) * f(18, 3) + f(80, 38) * f(38, 3) \
      - f(80, 38) * f(38, 18) * f(18, 3))
