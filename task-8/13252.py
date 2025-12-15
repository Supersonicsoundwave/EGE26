from itertools import permutations


alph = 'КИДАЛА'
cnt = 0
for val in set(permutations(alph, r=5)):
    val = ''.join(val)
    if 'АА' not in val:
        cnt += 1
print(cnt)
