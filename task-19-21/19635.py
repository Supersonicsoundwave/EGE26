def f(s1, s2, cnt):
    if s1 + s2 <= 100:
        return cnt % 2 == 0
    if cnt == 0:
        return False
    h = [f(s1 - 3, s2 - 3, cnt - 1),
         f(s1 // 2, s2, cnt - 1),
         f(s1, s2 // 2, cnt - 1)]
    return any(h) if (cnt - 1) % 2 == 0 else all(h)


print('19)', [s2 for s2 in range(53, 1000) if f(48, s2, 2)])  # 59
print('20)', [s2 for s2 in range(53, 1000) if f(48, s2, 3) and not f(48, s2, 1)])
print('21)', [s2 for s2 in range(53, 1000) if f(48, s2, 4) and not f(48, s2, 2)])
