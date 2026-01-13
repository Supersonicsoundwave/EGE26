from itertools import product
from string import printable


cnt = 0
for val in product(printable[:9], repeat=7):
    val = ''.join(val)
    if val[0] != '0' and '2' not in val:
        if len(set(val)) == len(val):
            for i in printable[:9]:
                if int(i, 9) % 2 == 0:
                    val = val.replace(i, '*')
                else:
                    val =val.replace(i, '!')
            if '**' not in val and '!!' not in val:
                cnt += 1
print(cnt)
