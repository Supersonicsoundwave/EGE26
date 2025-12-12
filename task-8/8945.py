from itertools import product
from string import printable


# 0 1 2 3 4 5 6 7 8 9 10 11
var1 = '*!*!*!*'  # * - 0 3 6 9 -> 3 8 4 8 4 8 4 -> 3 * 8^3 * 4^3
var2 = '!*!*!*!'  # ! - 1 2 4 5 7 8 10 11 -> 8 4 8 4 8 4 8 -> 8^4 * 4^3
print(3 * (8 ** 3) * (4 ** 3) + (8 ** 4) * (4 ** 3))

# или

cnt = 0
for val in product(printable[:12], repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        new_val = ''
        for i in val:
            if int(i, 12) % 3 == 0:
                new_val += '*'
            else:
                new_val += '!'
        if '!!' not in new_val and '**' not in new_val:
            cnt += 1
print(cnt)
