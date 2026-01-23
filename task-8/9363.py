from itertools import permutations
from math import factorial


print(factorial(12) - 8 * factorial(5) * factorial(7))

# НЕ ЗАПУСКАТЬ КОМП СДОХНЕТ
cnt = 0
for val in permutations('Х*Ч*Н*Б*ДЖ*Т'):
    val = ''.join(val)
    if '*****' not in val:
        cnt += 1
print(cnt)
