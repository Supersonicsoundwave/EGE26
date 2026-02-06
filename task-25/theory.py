# Задачи с масками

# Библиотека для проверки строк под маску
from fnmatch import fnmatch

# ? - ровно один любой символ
# * - любое кол-во любых символов

print(fnmatch('', '*'))


# КомпЕГЭ 4603 (рекомендованное решение)
from fnmatch import fnmatch

for N in range(12347 - 12347 % 141, 10 ** 8 + 1, 141):
   if fnmatch(str(N), '1234*7'):
       print(N, N // 141)

#########################################
print('#################')

# КомпЕГЭ 4603 (решение перебором)
from itertools import product

for l in range(0, 4):
    for val in product('0123456789', repeat=l):
        val = '1234' + ''.join(val) + '7'
        if int(val) % 141 == 0:
            print(val, int(val) // 141)

# проверка чисел на простоту
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

# Разложение числа на простые множители (медленный способ)
def fact_1(num):
    d = []

    for i in range(2, int(num ** .5 ) + 1):
        while num % i == 0:
            d += [i]
            num //= i

    if num > 2:
        d += [num]

    return d

# Разложение числа на простые множители (менее медленный способ)
def fact_2(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    for i in range(3, int(num ** .5) + 1, 2):
        while num % i == 0:
            d += [i]
            num //= i

    if num > 2:
        d += [num]

    return d

# Разложение числа на простые множители (быстрый способ)
def fact_3(num):
    d = []
    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d
