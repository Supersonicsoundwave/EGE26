from string import printable
from itertools import product


alph = printable[:15]
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1 and sum(map(lambda x: int(int(x, 15) > 9), val)) >= 2:
        cnt += 1
print(cnt)


# sum([val.count(x) for x in printable[10:15]])
