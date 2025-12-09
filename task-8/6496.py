from itertools import product

alph = 'БЕРСК'
cnt = 0
for rep in range(5, 8):
    for val in product(alph, repeat=rep):
        cnt += 1
print(cnt)
