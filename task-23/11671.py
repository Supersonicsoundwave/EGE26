def f1(cur, cnt=0):
    if cnt == 15:
        return {cur}
    return f1(cur + 10, cnt + 1) | f1(cur - 5, cnt + 1)

##############################################################

print(len(f1(1)))

def f(cur, cnt=0):
    global spots
    if cnt == 15:
        spots |= {cur}
        return
    f(cur + 10, cnt + 1)
    f(cur - 5, cnt + 1)


spots = set()

f(1)
print(len(spots))
