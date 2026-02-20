from itertools import permutations


cnt = 0
for val in set(permutations('ПРОСТО')):
    val = ''.join(val)
    if 'ОО' not in val:
        cnt += 1
print(cnt)
