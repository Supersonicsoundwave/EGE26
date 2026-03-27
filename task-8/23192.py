from itertools import product


alph = sorted('ТЕОРИЯ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    if pos % 2 != 0:
        val = ''.join(val)
        if val[0] not in 'РТЯ' and val.count('И') >= 2:
            print(pos)
