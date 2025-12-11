from itertools import product
from string import printable


alph = printable[:16]
cnt = 0
for val in product(alph, repeat=4):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') == 1:
        for i in val:
            if '**' in val.replace(i, '*'):
                break
        else:
            cnt += 1
print(cnt)
