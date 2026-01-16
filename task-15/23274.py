def f(x, y):
    return (2 * x + y != 110) or (x < y) or (a < x)


for a in range(1000, -1, -1):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break

