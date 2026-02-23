spots = set()


def f(cur, cnt=0):
    global spots
    if cnt > 15:
        return 0
    if cnt == 15:
        spots |= {cur}
        return 1
    return f(cur + 10, cnt + 1) + f(cur - 5, cnt + 1)


f(1)
print(len(spots))
