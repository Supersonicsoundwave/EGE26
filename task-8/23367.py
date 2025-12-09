from string import printable
from itertools import product

alph = printable[:7]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1:
        for i in alph:
            if '**' in val.replace(i, '*'):
                break
        else:
            cnt += 1
print(cnt)
