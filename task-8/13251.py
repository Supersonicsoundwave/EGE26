from itertools import permutations


cnt = 0
for val in permutations('КАЙФ'):
    val = ''.join(val)
    if val[-1] != 'Й' and 'КФ' not in val:
        cnt += 1

print(cnt)

