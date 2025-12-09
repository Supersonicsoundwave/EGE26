from string import printable
from itertools import product

alph = printable[:7]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] in '246' and val[-1] not in '012' and val.count('4') <= 1:
        cnt += 1
print(cnt)
