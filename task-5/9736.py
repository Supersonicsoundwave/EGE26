def f(n):
    r = f'{n:b}'
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += f'{(n % 3) * 3:b}'
    return int(r, 2)


ans = []
for n in range(1, 1000):
    if f(n) <= 170:
        ans.append(f(n))
print(max(ans))

