from itertools import permutations


alph = 'РОСОМАХА'
cnt = 0
for val in set(permutations(alph, r=8)):
    val = ''.join(['*' if letter in 'ОА' else '!' for letter in val])
    if '**' not in val and '!!' not in val:
        cnt += 1
print(cnt)

