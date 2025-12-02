from itertools import *

# product - функция, которая формирует все возможные комбинации символов длиной repeat (111, 112, 121 ...)
alph = '12'
for val in product(alph, repeat=3):
    val = ''.join(val)

# permutations - функция, которая формирует все возможные перестановки символов (12, 21)
for val in permutations(alph):
    val = ''.join(val)

# enumerate - нумерует элементы последовательности от start
alph1 = 'PRIVET'
res = enumerate(alph1, start=1)
print(*res) # (1, 'P') (2, 'R') (3, 'I') (4, 'V') (5, 'E') (6, 'T')
