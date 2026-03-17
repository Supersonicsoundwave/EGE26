# решать руками

def f(x):
    return not ((x % 263 == 0) <= (x % a == 0)) and (x % 71 == 0)


for a in range(20000, 0, -1):
    if all(not f(x) for x in range(1, 1000)):
        print(a)
        break
