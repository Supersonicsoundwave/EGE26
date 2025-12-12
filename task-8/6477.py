from itertools import permutations


alph = 'ЛЕВИОСА'
cnt = 0
for val in set(permutations(alph)):
    val = ''.join(val)
    if val[0] not in 'ЕИОА' and val[3] not in 'ЛВС':
        cnt += 1
print(cnt)
