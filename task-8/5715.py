from itertools import product


alph = 'КПБ'
combinations = []
for rep in range(1, 16):
    for val in product(alph, repeat=rep):
        val = ''.join(val)
        candies = val.count('К')
        cookies = val.count('П')
        candy_bars = val.count('Б')
        if candies > cookies > candy_bars:
            combination = f'{candies}{cookies}{candy_bars}'
            if combination not in combinations:
                combinations += [combination]
print(len(combinations))
