from itertools import product


alph = sorted('АРГУМЕНТ')
for pos, val in enumerate(product(alph, repeat=4), start=1):
    if len(set(val)) == 4 and sorted(val) == list(val):
        print(pos)
