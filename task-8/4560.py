from itertools import permutations


cnt = 0
for val in set(permutations('ТИХОРЕЦК', r=4)):
    val = ''.join(val)
    cond1 = sum([1 for symb in val[:4] if symb == 'ТИХО'[val.index(symb)]]) == 2
    for i in 'ИОЕ':
        val = val.replace(i, '*')
    cond2 = val.count('*') == 2
    if cond1 and cond2:
        cnt += 1
print(cnt)
