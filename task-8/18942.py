from itertools import product

alph = 'ДИОНСЙ'
cnt = 0
for val in product(alph, repeat=6):
    val = ''.join(val)
    if 'Д' in val and 'Н' in val:
        continue
    double = False
    for letter in alph:
        if letter * 2 in val:
            double = True
    if ('Д' in val or 'Н' in val) and not double:
        cnt += 1
print(cnt)
