def f(x, y):
    return (x * y > a) or (x > y) or (11 > x)


for a in range(1000, -1, -1):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break
