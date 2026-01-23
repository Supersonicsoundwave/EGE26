from string import printable
from itertools import permutations


cnt = 0
for val in set(permutations(printable[:8], r=6)):
    val = ''.join(val)
    if val[0] != '0' and int(val, 8) % 5 == 0:
        for i in printable[:8]:
            if int(i) % 2 == 0:
                val = val.replace(i, '*')
            else:
                val = val.replace(i, '!')
        if '**' not in val and '!!' not in val:
            cnt += 1
print(cnt)
