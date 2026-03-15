def f(cur, end):
    if cur > end or cur == 24:
        return 0
    if cur == end:
        return 1
    return f(cur + 1, end) + f(cur + 2, end) + f(cur + 4, end) + f(cur + 8, end)


# print(f(16, 24) * f(24, 48))  11428032
print(f(16, 32) * f(32, 48))  # 11253585
print(11428032 + 11253585)
