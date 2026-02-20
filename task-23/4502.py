def f(cur, end, cnt):
    if cur == end and cnt == 6:
        return 1
    if cur > end or cnt > 6:
        return 0
    return f(cur + 1, end, cnt + 1) + f(cur + 2, end, cnt + 1) + f(cur * 2, end, cnt + 1)


k = 0
for end in range(34, 59 + 1):
    if f(1, end, 0):
        k += 1
print(k)
