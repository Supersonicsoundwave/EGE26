from itertools import product


cnt = 0
for val in product('ПИТОН', repeat=4):
    maket = list(map(lambda x: '1' if x in 'ИО' else '2', val))
    maket = ''.join(maket)
    if '11' not in maket and '22' not in maket:
        cnt += 1
print(cnt)
