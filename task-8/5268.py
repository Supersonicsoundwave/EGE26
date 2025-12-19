from itertools import permutations


alph = 'АМФИБРАХИЙ'
cnt = 0
for val in set(permutations(alph)):
    val = ''.join(val)
    if 'ИИФАА' in val or 'ААФИИ' in val:
        cnt += 1
print(cnt)
