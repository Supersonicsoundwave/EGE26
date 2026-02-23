spots = set()


def f(cur, cnt=0):
    global spots
    if cnt == 8:
        if 1000 <= cur <= 1024:
            spots |= {cur}
            return 1
        return 0
    return f(cur + 1, cnt + 1) + f(cur + 5, cnt + 1) + f(cur * 3, cnt + 1)


f(1)
print(len(spots))
