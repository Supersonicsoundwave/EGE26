from itertools import product


alph1 = 'КОНЕЦ'
alph2 = 'ДРАКОН'
list1 = [''.join(val) for val in product(alph1, repeat=5)]
list2 = [''.join(val) for val in product(alph2, repeat=5)]
cnt = 0

for val in list1:
    if val not in list2:
        cnt += 1
    else:
        list2.remove(val)

cnt += len(list2)
print(cnt)
