from itertools import permutations


alph = 'ЗАПИСЬ'
cnt = 0
for val in set(permutations(alph)):
    val = ''.join(val)
    if val[0] != 'Ь' and 'АЬ' not in val and 'ИЬ' not in val:
        cnt += 1
print(cnt)
