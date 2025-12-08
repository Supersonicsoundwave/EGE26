from itertools import product


alph = 'АЛГОРИТМ'
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if val.count('Л') < 2 and val[0] != 'Р' and val[-1] not in 'ЛГРТМ':
        cnt += 1
print(cnt)
