from itertools import *


alph = sorted('ДОСЖ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[:2] == 'ЖС':
        print(pos)
        break