from itertools import permutations


graph = 'ГЕ ЕК КД ДБ БА БВ ВГ ВЕ ЕД ДВ'.split()
matrix = '27 1567 67 5 246 2357 1236'.split()
print(*range(1, 8))
for i in permutations('АБВГДЕК'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
