from itertools import product
from string import printable


alph = printable[:12]
cnt = 0
for val in product(alph, repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('b') == 2 and '**' not in ''.join(['*' if i in '02468a' else '!' for i in val]) and \
                '!!' not in ''.join(['*' if i in '02468a' else '!' for i in val]):
            cnt += 1
print(cnt)
