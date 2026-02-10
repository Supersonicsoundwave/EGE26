from fnmatch import fnmatch


def f(num):
    d = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            d |=  {num // i, i}
    if len(d) > 30:
        return sum(d)
    return 0


for n in range(202 - 202 % 53, 10**7 + 1, 53):
    if str(n) == str(n)[::-1] and fnmatch(str(n), '*2?2*'):
        if sm := f(n):
            print(n, sm)

