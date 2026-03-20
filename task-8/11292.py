from string import printable
from itertools import product


cnt = 0
for val in product(printable[:16], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 2:
        for i in printable[:16:2]:
            if i != '6':
                val = val.replace(i, '*')
        if '*6' not in val and '6*' not in val and '66' not in val:
            cnt += 1

print(cnt)
