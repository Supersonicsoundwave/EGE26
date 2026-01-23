def f(x, y):
    return (x + y <=  32) or (y <= x + 4) or (y >= a)


for a in range(1000, -1, -1):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
