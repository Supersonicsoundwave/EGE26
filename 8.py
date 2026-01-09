from string import printable
from itertools import product


alph = printable[:25]
cnt = 0
# for val in list(product(alph, repeat=4))[500:1000]:
#     val = ''.join(val)
#     if val[0] != '0':
#         if sum(1 for x in val if int(x, 25) % 2 != 0) == 1 and sum(1 for x in val if int(x, 25) <= 5) <= 2:
#             print(val)
#             cnt += 1
# # print(cnt)
#
# print()
cnt = 0
for val in list(product(alph, repeat=4)):
    val = ''.join(val)
    if val[0] != '0':
        nech = 0
        for num in val:
            if int(num, 25) % 2 != 0:
                nech += 1
        if nech == 1:
            for i in '012345':
                val = val.replace(i, '*')
            if val.count('*') <= 2:
                cnt += 1
print(cnt)
