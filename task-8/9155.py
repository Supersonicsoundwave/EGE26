from itertools import product


alph = sorted('АПРЕЛЬ', reverse=True)
cnt = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos <= 387 and val[-1] == 'Ь':
        cnt += 1
print(cnt)
