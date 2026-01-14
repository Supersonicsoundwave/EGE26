def f(x):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + a >= 80)


for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break