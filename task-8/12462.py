from string import printable
from itertools import product


cnt = 0
for k in 3, 5:
    for val in product(printable[:16], repeat=k):
        val = ''.join(val)
        if val[0] != '0':
            if len(val) == 3:
                if int(val[0], 16) > int(val[1], 16) > int(val[2], 16):
                    cnt += 1
            else:
                if int(val[0], 16) > int(val[1], 16) > int(val[2], 16) > int(val[3], 16) > int(val[4], 16):
                    cnt += 1
print(cnt)
