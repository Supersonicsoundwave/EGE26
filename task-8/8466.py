from itertools import product
from string import printable


alph = printable[:7]
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val != '0':
        if val[-1] not in '0123' and sum([1 if int(x) % 2 != 0 else 0 for x in val]) == 3:
            cnt += 1
print(cnt)

