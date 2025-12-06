from re import *

with open(r'.\files\24_865.txt') as file:
    data = file.readline()

cnt = 0
mx_len = 0
for i in data:
    if i in 'CF':
        mx_len = max(cnt, mx_len)
        cnt = 0
    else:
        cnt += 1
mx_len = max(cnt, mx_len)
print(mx_len)


pattern = r'[^CF]+'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)))


for symb in 'CF':
    data = data.replace(symb, ' ')
data = data.split()
print(len(max(data, key=len)))
