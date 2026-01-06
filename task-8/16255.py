from itertools import product


cnt = 0
for val in product('012345678', repeat=7):
    val = ''.join(val)
    if val[0] not in '01357':
        if '6' in val and val[-1] in '124578':
            cnt += 1
print(cnt)
