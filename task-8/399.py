from itertools import permutations


alph = 'ВОРОТА'
cnt = 0
for val in set(permutations(alph, r=6)):
    val = ''.join(val)
    val = val.replace('А', '*')
    val = val.replace('О', '*')
    if '**' not in val:
        cnt += 1
print(cnt)
