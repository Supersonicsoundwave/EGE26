def f(s1, s2, cnt):
    if s1 * s2 > 384:
        return cnt % 2 == 0
    if cnt == 0:
        return False
    h = [f(s1 + 5, s2, cnt - 1),
         f(s1 * 2, s2, cnt - 1),
         f(s1, s2 + 5, cnt - 1),
         f(s1, s2 * 2, cnt - 1)]
    return any(h) if (cnt - 1) % 2 == 0 else all(h)


print('19)', [s2 for s2 in range(1, 55) if f(8, s2, 2)])
print('19)', [s2 for s2 in range(1, 55) if f(8, s2, 3) and not f(8, s2, 1)]) # 13
print('19)', [s2 for s2 in range(1, 55) if f(8, s2, 4) and not f(8, s2, 2)])
