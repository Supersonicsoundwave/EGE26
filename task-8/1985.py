from itertools import permutations


cnt = 0
for val in permutations('АБИКОЛУН', r=8):
    val = ''.join(val)
    for i in 'АБИКОЛУН':
        if i in 'АИОУ':
            val = val.replace(i, '*')
        else:
            val = val.replace(i, '!')
    if '**' not in val and '!!' not in val:
        cnt += 1
print(cnt)
