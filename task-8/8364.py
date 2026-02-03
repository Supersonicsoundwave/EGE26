from itertools import product


alph = sorted('КРАТЕ')
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val == 'КАРЕТА':
        start = pos
    if val == 'РАКЕТА':
        end = pos
print(end - start - 1)
