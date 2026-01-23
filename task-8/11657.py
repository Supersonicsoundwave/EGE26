from string import printable
from itertools import product


cnt = 0
for val in product(printable[:8], repeat=6):
    val = ''.join(val)
    if val[0] != '0' and '3' not in val:
        if  len(set(val)) == len(val):
            for i in '0246':
                val = val.replace(i, '*')
            if '**' in val:
                cnt += 1
print(cnt)
