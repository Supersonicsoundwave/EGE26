def f(x):
    B = 70 <= x <= 90
    return (x % a == 0) or (B <= (x % 22 != 0))


for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
