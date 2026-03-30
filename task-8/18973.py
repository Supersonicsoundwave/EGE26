from string import printable
from itertools import product


alph = printable[:25]
cnt = 0
for val in product(alph, repeat=4):
    val = ''.join(val)
    if val[0] != '0':
        chet = [int(num, 25) % 2 == 0 for num in val]
        bigger15 = [int(num, 25) > 15 for num in val]
        if sum(chet) and sum(bigger15) > 2:
            cnt += 1
print(cnt)
