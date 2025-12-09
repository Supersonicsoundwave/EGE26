from itertools import product

alph = 'МОЛЬ'
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if 'Ь' in val:
        if val.count('МЬ') + val.count('ЛЬ') == val.count('Ь'):
            cnt += 1
    else:
        cnt += 1
print(cnt)
