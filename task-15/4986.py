def f(x):
    return (x % a == 0) or ((x % 23 == 0) <= (not 50 <= x <= 70))


for a in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
