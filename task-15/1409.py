def f(x):
    P = x in range(2, 21, 2)
    Q = x in range(3, 31, 3)
    R = x in range(12, 61, 12)
    return (x not in A) <= ((P and Q) <= R)


A = []
for x in range(2, 61):
    if not f(x):
        A += [x]
print(A)
