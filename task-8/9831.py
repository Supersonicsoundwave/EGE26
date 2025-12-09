from string import printable
from itertools import product


cnt = 0
alph = printable[:16]
for val in product(alph, repeat=3):
    val = ''.join(val)
    if val[0] != '0' and len(set(val)) ==  len(val):
        val = ''.join(map(lambda x: '*' if int(x, 16) % 2 == 0 else '!', val))
        if '!!' not in val and '**' not in val:
            cnt += 1
print(cnt)
