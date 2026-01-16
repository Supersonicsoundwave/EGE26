def f(x, y):
    return (9 * x + y > a) or (x >= 36) or (y >= 18)


for a in range(1000, 0, -1):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
