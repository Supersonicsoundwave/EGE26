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
