from re import *


with open(r'.\files\24_1874.txt') as file:
    data = file.readline()

pattern = r'(?<=Q)W.+?Q(?=W)'
res = [match.group() for match in finditer(pattern, data)]
print(len(max(res, key=len)))


cnt = 1
mx_len = 0
for i in range(len(data) - 1):
    if data[i] + data[i + 1] == 'QW':
        mx_len = max(mx_len, cnt)
        cnt = 1
    else:
        cnt += 1
print(mx_len)


data = data.replace('QW', ' ')
data = data.split()
print(len(max(data, key=len)))