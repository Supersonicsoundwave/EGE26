from string import printable
from itertools import product


alph = printable[:8]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] not in '01357' and val[-1] not in '26' and val.count('7') <= 2:
        cnt += 1
print(cnt)
