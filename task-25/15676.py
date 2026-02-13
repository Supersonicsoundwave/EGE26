from fnmatch import fnmatch
from itertools import product



def not_prime(num):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return True
    return False


sost = []
for i in range(4, 1000):
    if not_prime(i):
        sost += [i]


for i in range(22768, 10**8, 22768):
    for N in sost:
        if fnmatch(str(i), f'1{N}03*6*'):
            print(i, N)

################################################

ans = []
for l1 in range(1, 5):
    for N in range(10 ** (l1 - 1), 10 ** l1):
        if not_prime(N):
            for l2 in range(0, 4 - l1 + 1):
                for Z1 in product('0123456789', repeat=l2):
                    Z1 = ''.join(Z1)
                    for l3 in range(0, 4 - l1 - l2 + 1):
                        for Z2 in product('0123456789', repeat=l3):
                            Z2 = ''.join(Z2)
                            num = int(f'1{N}03{Z1}6{Z2}')
                            if num % 22768 == 0 and num < 10**8:
                                ans += [(num, N)]
ans.sort(key=lambda x: x[0])
for i in ans:
    print(*i)

