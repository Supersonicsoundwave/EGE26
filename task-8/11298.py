from itertools import *


alph = sorted('АОЖПЮЗ')
cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[0] == 'А' and val.count('З') >= 2 and pos % 2 == 0:
        cnt += 1
print(cnt)