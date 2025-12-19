from itertools import permutations


graph = 'HF FE ED DG GA AH HB BF BC CG'.split()
matrix = '478 38 256 15 34 37 168 127'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
