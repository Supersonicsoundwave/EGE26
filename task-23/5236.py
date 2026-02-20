def f(cur, end, cnt):
    if cur not in [2, 400]:
        cnt += 1
    if cur == end and cnt > 50:
        return 1
    if cur > end:
        return 0
    return f(cur + 2, end, cnt) + f(cur * 3, end, cnt) + f(cur * 4, end, cnt)


print(f(2, 400, 0))
