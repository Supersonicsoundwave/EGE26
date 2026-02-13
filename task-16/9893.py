from sys import setrecursionlimit


def f(n):
    if n < 3:
        return 3
    return 2 * n + 5 + f(n - 2)


setrecursionlimit(2000)
print(f(3027) - f(3023))
