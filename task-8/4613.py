from string import printable
from itertools import product


alph = printable[:9]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] not in '01357' and val[-1] not in '18' and val.count('3') <= 1:
        cnt += 1
print(cnt)
