from itertools import *


alph = sorted('ГИРЛЯНДА')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] != 'Я' and val.count('Д') == 3:
        print(pos)