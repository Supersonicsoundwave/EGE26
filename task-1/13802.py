from itertools import permutations


graph = 'EH HG GC CF FA AE DE DB DF BH BG'.split()
matrix = '367 568 18 58 247 127 156 234'.split()
print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i, sep=' ')