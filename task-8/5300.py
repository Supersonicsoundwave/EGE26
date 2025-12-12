from itertools import permutations


alph = 'ХОЧУ В ВУЗ'
cnt = -1
for val in set(permutations(alph)):
    val = ''.join(val)
    if val[0] not in ' У' and val[-1] != ' ' and '  ' not in val and ' У' not in val:
        cnt += 1
print(cnt)
