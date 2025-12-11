from itertools import product

alph = sorted('СУБЛИМАЦЯ')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[-1] != 'Я' and sum(map(lambda x: int(x in 'УИАЯ'), val)) == 2:
        print(pos)
