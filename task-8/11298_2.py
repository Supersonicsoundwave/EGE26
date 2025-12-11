from itertools import product


alph = sorted('АОЖПЮЗ')
cnt = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if pos % 2 == 0 and val[0] == 'А' and val.count('З') >= 2:
        cnt += 1
print(cnt)
