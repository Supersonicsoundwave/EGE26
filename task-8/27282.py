from string import printable
from itertools import product


cnt = 0
for val in product(printable[:13], repeat=6):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('0') >= 2:
            for i in set(val):
                if int(i, 13) > 9:
                    val = val.replace(i, '*')
            if val.count('*') == 2 and '**' in val:
                cnt += 1
print(cnt)