from itertools import product
from string import printable


alph = printable[:20]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if int(val[0], 20) + int(val[-1], 20) == 26:
            for i in alph:
                if int(i, 20) % 2 == 0:
                    val = val.replace(i, '*')
                else:
                    val = val.replace(i, '!')
            if '!!' not in val and '**' not in val:
                cnt += 1
print(cnt)
