from itertools import permutations


graph = 'BD DE EA AC CG GB GF FE FC'.split()
matrix = '26 147 456 237 37 13 245'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
