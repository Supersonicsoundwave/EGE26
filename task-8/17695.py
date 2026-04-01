from itertools import product


cnt = 0
alph = '0123456'
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0':
        if sum(num in '345' for num in val) == 2 and all(val[i] != val[i + 1] for i in range(4)):
            cnt += 1
print(cnt)
