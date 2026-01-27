def f(x):
    B = 80 <= x <= 100
    return (x % 17 == 0) <= (not B or (a < x + 30))


for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
