def convert10(num, q):
    ans = 0
    for i in range(len(num)):
        ans += num[i] * q ** i
    return ans


res = set()
for x in range(10, 67):
    for y in range(x):
        a = convert10([7, 3, x, 1, y], 67)
        b = convert10([4, 9, y, 6], x)
        f = a + b
        res.add(f)
print(len(res))
