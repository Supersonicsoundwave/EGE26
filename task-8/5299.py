from itertools import permutations


alph = 'ХОЧУ СОТКУ'
cnt = -1
for val in set(permutations(alph)):
    val = ''.join(val)
    if val[0] not in ' У' and val[-1] != ' ' and ' У' not in val:
        cnt += 1
print(cnt)
