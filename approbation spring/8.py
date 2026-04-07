from itertools import product


cnt = 0
for val in product('0123456', repeat=7):
    val = ''.join(val)
    if val[0] not in '035':
        if sum(s in val for s in ['22', '44']) < 2:
            cnt += 1

print(cnt)
