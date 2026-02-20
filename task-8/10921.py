from itertools import permutations


cnt = 0
for val in set(permutations('ДЖАВАСКРИПТ')):
    val = ''.join(val)
    k = 3
    for i in range(len(val)):
        if val[i] in 'АИ':
            k += i
    if k == 11:
        cnt += 1
print(cnt)
