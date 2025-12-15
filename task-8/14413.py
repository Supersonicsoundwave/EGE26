from itertools import permutations


alph = 'СОРТИРОВКА'
cnt = 0
for val in set(permutations(alph)):
    val = ''.join(val)
    for i in val:
        if i in 'СРТРВК':
            val = val.replace(i, '!')
        else:
            val = val.replace(i, '*')
    if '!!!' not in val and '***' not in val:
        cnt += 1
print(cnt)
