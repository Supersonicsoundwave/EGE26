from itertools import product


alph = sorted('СТРОКА')
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] not in 'АЛ' and val.count('С') == 1:
        print(pos)

