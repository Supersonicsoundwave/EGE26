def f(a):
    for x in range(1000):
        for y in range(1000):
            f = (2 * x + y != 70) or (x < y) or (a < x)
            if not f:
                return False
    return True


for a in range(1000, -1000, -1):
    if f(a):
        print(a)
        break

#################################################################

def f(x, y):
    return (2 * x + y != 70) or (x < y) or (a < x)


for a in range(1000, -1000, -1):
    if all(f(x, y) for x in range(1000) for y in range(1000)):
        print(a)
        break
