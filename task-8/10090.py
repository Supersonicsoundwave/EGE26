from itertools import permutations


cnt = 0
for val in permutations('0234567', r=5):
    val = ''.join(val)
    if val[0] !='0':
        for i in '0234567':
            if int(i) % 2 == 0:
                val = val.replace(i, '*')
            else:
                val = val.replace(i, '!')
        if '!!' not in val and '**' not in val:
            cnt += 1
print(cnt)
