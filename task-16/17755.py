def f(n):
    if n > 400:
        return n ** n
    return n + 6 + f(n + 12)


for i in range(412, 71, -1):
    f(i)

print(f(72) - f(108))

