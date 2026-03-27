from sys import setrecursionlimit


def f(n):
    if n <= 5:
        return 1
    return n + f(n - 2)


setrecursionlimit(1100)
print(f(2126) - f(2122))

#######################################

cache = [0] * 2200
for i in range(2200):
    if i <= 5:
        cache[i] = 1
    else:
        cache[i] = i + cache[i - 2]

print(cache[2126] - cache[2122])
