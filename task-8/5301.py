from itertools import product


# неверно
alph = 'ЛЕСЯ '
cnt = 0
for val in product(alph, repeat=5):
    val = ''.join(val)
    if len(val.split()) == 2 and '**' not in ''.join(['*' if i in 'ЕЯ' else '_' for i in val]) \
            and '!!' not in ''.join(['!' if i in 'ЕЯ' else '_' for i in val]):
        cnt += 1
print(cnt)


