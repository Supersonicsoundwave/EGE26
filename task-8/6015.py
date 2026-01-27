from string import printable
from itertools import product


cnt = 0
for val in product(printable[:9], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('8') == 1 and val[0] not in '1357' and val[-1] not in '02468':
            cnt += 1
print(cnt)

