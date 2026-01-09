from itertools import product


alph = sorted('НОРМАЛЬЕ')
start = 0
end = 0
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if val[:6] == 'НЕНОРМ' and not start:
        start = pos
    if val[:4] == 'НОРМ' and not end:
        end = pos

print(end - start - 1)
