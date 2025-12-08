from itertools import product


alph = 'ПОЛИНА'
cnt = 0
for val in product(alph, repeat=8):
    val = ''.join(val)
    if sum(map(lambda x: int(x in 'ПЛН'), val)) > sum(map(lambda x: int(x in 'ОИА'), val)):
        cnt += 1
print(cnt)
