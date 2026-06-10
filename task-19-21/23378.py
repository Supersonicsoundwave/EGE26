def f(s, cnt):
    if s <= 27:
        return cnt % 2 == 0
    if cnt == 0:
        return False
    h = [f(s - 3, cnt - 1),
         f(s - 6, cnt - 1),
         f(s // 3, cnt - 1)]
    return any(h)  if (cnt - 1) % 2 == 0  else all(h)


print('19)', [s for s in range(28, 1000) if f(s, 2)])
print('20)', [s for s in range(28, 1000) if f(s, 3) and not f(s, 1)])
print('21)', [s for s in range(28, 1000) if f(s, 4) and not f(s, 2)])
