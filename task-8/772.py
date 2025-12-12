from itertools import permutations


alph = 'ПРОБНИК'
cnt = 0
for val in set(permutations(alph, r=7)):
    val = ''.join(val)
    for i in val:
        if i in 'ПРБНК':
            val = val.replace(i, '!')
        else:
            val = val.replace(i, '*')
    if val[0] == '!' and val[-1] == '!' and '**' not in val:
        cnt += 1
print(cnt)
