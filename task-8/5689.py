from itertools import product


alph = '01'
cnt = 0
for val in product(alph, repeat=16):
    val = ''.join(val)
    if val[0] != '0':
        if val.count('1') % 3 == 0:
            cnt += 1
print(cnt)
