from itertools import product


alph = sorted('АВТОР')
for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    if val == 'ВАТА':
        print(pos)
        break