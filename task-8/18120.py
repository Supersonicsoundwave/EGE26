from itertools import product


alph = sorted('ПРЕСТОЛ')
cnt = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if pos % 2 != 0:
        for i in 'ПРСТЛ':
            val = val.replace(i, '*')
        if val.count('*') <= 3 and val[-1] != '*':
            cnt += 1
print(cnt)
