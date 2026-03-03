def f(s1, s2, cnt):
    if s1 + s2 <= 108:
        return cnt % 2 == 0
    if cnt == 0:
        return False
    h = [
        f(s1 - 2, s2, cnt - 1),
        f((s1 + 1) // 2, s2, cnt - 1),
        f(s1, s2 - 2, cnt - 1),
        f(s1, (s2 + 1) // 2, cnt - 1)
    ]
    return any(h) if (cnt - 1) % 2 == 0 else all(h)



