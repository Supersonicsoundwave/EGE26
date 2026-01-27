from string import printable
from itertools import product


cnt = 0
for val in product(printable[10:16], repeat=6):
    val = ''.join(val)
    if val[0] not in 'ae' and val[-1] not in 'ae':
        cnt += 1
print(cnt)
