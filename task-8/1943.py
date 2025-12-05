from itertools import product

cnt = 0
for val in product('ЗЕРКАЛО', repeat=6):
    val = ''.join(val)
    if 1 <= val.count('К') <= 4 and len(set(val)) + val.count('К') - 1 == len(val):
        cnt += 1
print(cnt)
