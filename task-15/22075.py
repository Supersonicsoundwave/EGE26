def dig(x, y):
    return True if str(x)[0] == str(y)[0] else False


def f(x):
    return (not dig(x, 28) and dig(x, 47)) <= (x > A - 20)


for A in range(1000, 0, -1):
    if all(f(x) for x in range(1, 1000)):
        print(A)
        break
