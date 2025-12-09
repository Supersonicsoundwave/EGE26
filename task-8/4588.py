from string import printable
from itertools import product


cnt = 0
alph = printable[:8]
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1:
        val = ''.join(map(lambda x: '!' if int(x, 8) % 2 != 0 else x, val))
        if '!6' not in val and '6!' not in val:
            cnt += 1
print(cnt)
