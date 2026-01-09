from functools import *


def H(p):
    return [p + 1, p + 3, p * 2]


@lru_cache()
def f(p):
    if p >= 39:
        return 'L'
    return 'W' if any(f(h) == 'L' for h in H(p)) else 'L'


@lru_cache()
def c(p):
    if p >= 39:
        return 0
    if f(p) == 'W':
        return 1 + min(c(h) for h in H(p) if f(h) == 'L')
    return 1 + max(c(h) for h in H(p))


print('19', min(s for s in range(1, 39) if c(s) == 2))
print('20', [s for s in range(1, 39) if c(s) == 3])
print('21', min(s for s in range(1, 39) if c(s) == 4))

