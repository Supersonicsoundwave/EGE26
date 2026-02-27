def f(cur, cnt=0):
    global spots
    if cnt == 8:
        if 1000 <= cur <= 1024:
            spots |= {cur}
            return
        return
    f(cur + 1, cnt + 1)
    f(cur + 5, cnt + 1)
    f(cur * 3, cnt + 1)


spots = set()

f(1)
print(len(spots))

########################################################################

def f1(cur, cnt=0):
    if cnt == 8:
        if 1000 <= cur <= 1024:
            return {cur}
        return set()
    return f1(cur + 1, cnt + 1) | f1(cur + 5, cnt + 1) | f1(cur * 3, cnt + 1)


print(len(f1(1)))
