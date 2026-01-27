from fnmatch import fnmatch


for x in range(124065 - 124065 % 161, 10 ** 8 + 1, 161):
    if fnmatch(str(x), '12*4?65'):
        print(x, x // 161)

######################################################

from itertools import product
from string import printable

# 100000000
# 120004065
ans = []
for v in printable[:10]:
    for l in range(0, 3):
        for z in product(printable[:10], repeat=l):
            num = int(f'12{''.join(z)}4{v}65')
            if num % 161 == 0:
                ans += [(num, num // 161)]

for i in sorted(ans):
    print(*i)


