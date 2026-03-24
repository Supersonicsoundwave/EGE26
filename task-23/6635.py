otr = set()


def f(cur, cnt):
    global otr
    if cur < 0  and cnt == 13:
        otr |= {cur}
        return 1
    if cnt == 13 and cur >= 0:
        return 0
    return f(cur - 3, cnt + 1) + f(cur * (-3), cnt + 1)


f(333, 0)
print(len(otr))
