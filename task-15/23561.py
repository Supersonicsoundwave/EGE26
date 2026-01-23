def f(x):
    return (x % 128 == 0) <= ((x % a != 0) <= (x % 80 != 0))


for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
