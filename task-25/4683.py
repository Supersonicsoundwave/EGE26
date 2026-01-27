from fnmatch import fnmatch


for x in range(2123406 - 2123406 % 37, 10**8 + 1, 37):
    if fnmatch(str(x), '2*1234?6'):
        print(x, x // 37)

###################################################

from itertools import product
from string import printable

# 100000000
# 200123406
ans = []
for v in printable[:10]:
    for l in range(2):
        for z in product(printable[:10], repeat=l):
            num = int(f'2{''.join(z)}1234{v}6')
            if num % 37 == 0:
                ans += [(num, num // 37)]

for i in sorted(ans):
    print(*i)
