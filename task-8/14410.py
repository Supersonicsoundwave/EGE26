from itertools import *


cnt = 0
alph = sorted('СОЛНЦЕ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] not in 'ОЕ' and val.count('Ц') == 2:
        cnt += 1
print(cnt)
