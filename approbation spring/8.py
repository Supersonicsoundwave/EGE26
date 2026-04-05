from itertools import product


cnt = 0
for val in product('0123456', repeat=7):
    val = ''.join(val)
    if val[0] not in '035':
        if '22' not in val and '44' not in val:
            cnt += 1

print(cnt)
