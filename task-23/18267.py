def f(cur, end, s=''):
    if cur > end:
        return 0
    if cur == end:
        if s[-1] != 'C':
            return 1
        return 0
    return f(cur + 2, end, s + 'A') + f(cur + 5, end, s + 'B') + f(cur ** 2, end, s + 'C')


print(f(4, 36))
