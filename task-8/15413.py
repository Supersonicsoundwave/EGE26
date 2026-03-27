from itertools import product
from string import printable


cnt = 0
for val in product(printable[:9], repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1:
        left, right = val.split('8')
        if sum(int(i) for i in left) == sum(int(i) for i in right):
            cnt += 1
print(cnt)
