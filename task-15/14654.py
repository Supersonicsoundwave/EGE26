def f(x):
    return (x % a == 0) or ((x % 133 == 0) <= (x % 95 != 0))


for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
