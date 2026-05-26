def f(s1, s2, cnt):
    if s1 + s2 >= 207:
        return cnt % 2 == 0
    if cnt == 0:
        return False
    h = [f(s1 + 1, s2, cnt - 1),
         f(s1 * 2, s2, cnt - 1),
         f(s1, s2 + 1, cnt - 1),
         f(s1, s2 * 2, cnt - 1)]
    return any(h) if (cnt - 1) % 2 == 0 else all(h)


print('19)', [s2 for s2 in range(1, 190) if f(17, s2, 2)]) # 48
print('19)', [s2 for s2 in range(1, 190) if f(17, s2, 3) and not f(17, s2, 1)])
print('19)', [s2 for s2 in range(1, 190) if f(17, s2, 4) and not f(17, s2, 2)])
