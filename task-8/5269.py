from itertools import permutations


alph = 'АМФИБРАХИЙ'
cnt = 0
for val in set(permutations(alph)):
    val = ''.join(val)
    if val[len(val) // 2 - 1:len(val) // 2 + 1] == 'БР':
        cnt += 1
print(cnt)
