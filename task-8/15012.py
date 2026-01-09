from string import printable
from itertools import product


alph = printable[:14]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if len(set(val)) == 2 and val[-1] in '03':
            cnt += 1
print(cnt)
