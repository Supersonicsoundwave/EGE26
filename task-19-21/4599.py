def f(s1, s2, cnt):
    if s1 + s2 >= 259:
        return cnt % 2 == 0
    if cnt == 0:
        return 0
    h = [
        f(s1 + 1, s2,  cnt - 1),
        f(s1 * 2, s2,  cnt - 1),
        f(s1, s2 + 1, cnt - 1),
        f(s1, s2 * 2, cnt - 1),
    ]
    return any(h) if (cnt - 1) % 2 == 0 else all(h)


print('19)', [s2 for s2 in range(1, 242) if f(17, s2, 2)])  # 61 (меняем all на any)
print('20)', [s2 for s2 in range(1, 242) if f(17, s2, 3) and not f(17, s2, 1)])
print('21)', [s2 for s2 in range(1, 242) if f(17, s2, 4) and not f(17, s2, 2)])

