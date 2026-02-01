def f(x):
    return ((405 % x == 0) <= (81 % x == 0)) or (a - x > 162)


for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break