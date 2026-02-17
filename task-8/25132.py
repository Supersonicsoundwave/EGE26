from itertools import product

alph = sorted('СДАЙЕГЭ')
nums = []
for pos, val in enumerate(product(alph, repeat=6), start=1):
    val = ''.join(val)
    if 'ЕГЭ' in val:
        nums += [pos]
print(sum(nums))
