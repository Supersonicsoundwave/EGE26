from re import *


with open(r'.\files\24_864.txt') as file:
    data = file.readline()

cnt = 0
max_len = 0
for i in data:
    if i in 'AE':
        max_len = max(max_len, cnt)
        cnt = 0
    else:
        cnt += 1
max_len = max(max_len, cnt)
print(max_len)


pattern = r'[^AE]+'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)))


for symb in 'AE':
    data = data.replace(symb, ' ')
data = data.split()
print(len(max(data, key=len)))
